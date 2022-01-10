# Copyright 2020 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

"""Expansion of realms_config.Realm into a flat form."""

import collections

from components.auth.proto import realms_pb2
from components.config import validation as cfg_validation

from proto import realms_config_pb2

from realms import common
from realms import permissions
from realms import validation


def expand_realms(db, project_id, realms_cfg):
  """Expands realms_config_pb2.RealmsCfg into a flat realms_pb2.Realms.

  The returned realms_pb2.Realms contains realms and permissions of a single
  project only. Permissions not mentioned in the project's realms are omitted.
  All realms_pb2.Permission messages have names only (no metadata). api_version
  field is omitted.

  All such realms_pb2.Realms messages across all projects (plus a list of all
  defined permissions with all their metadata) are later merged together into
  a final universal realms_pb2.Realms by realms.merge(...) in
  components/auth/replication.py.

  Args:
    db: a permissions.DB instance with current permissions and roles.
    project_id: ID of a LUCI project to use as a prefix in realm names.
    realms_cfg: an instance of realms_config_pb2.RealmsCfg to expand.

  Returns:
    realms_pb2.Realms with expanded realms (with caveats mentioned above).

  Raises:
    ValueError if the validation fails.
  """
  # `internal` is True when expanding internal realms (defined in a service
  # config file). Such realms can use internal roles and permissions and they
  # do not have implicit root bindings (since they are not associated with
  # any "project:<X>" identity used in implicit root bindings).
  internal = project_id == common.INTERNAL_PROJECT

  # The server code could have changed since the config passed the validation
  # and realms_cfg may not be valid anymore. Verify it still is. The code below
  # depends crucially on the validity of realms_cfg.
  validation.Validator(
      cfg_validation.Context.raise_on_error(), db, internal,
  ).validate(realms_cfg)

  # Make sure @root realm exist and append implicit bindings to it. We need to
  # do it before enumerating conditions below to actually instantiate all
  # Condition objects that we'll need to visit (some of them may come from
  # implicit bindings). Pre-instantiating them is important because we rely
  # on their uniqne and stable id(...) for faster hash map lookups.
  realms_map = to_realms_map(
      realms_cfg,
      db.implicit_root_bindings(project_id) if not internal else [])

  # We'll need to visit realms in sorted order twice. Sort once and remember.
  realms_list = sorted(realms_map.items())

  # Prepopulate `conds_set` with all conditions mentioned in all bindings to
  # normalize, dedup and map them to integers. Integers are faster to work
  # with and we'll need them for the final proto message.
  conds_set = ConditionsSet()
  for _, realm in realms_list:
    for binding in realm.bindings:
      for cond in binding.conditions:
        conds_set.add_condition(cond)
  all_conditions = conds_set.finalize()

  # A lazily populated {role -> tuple of permissions} mapping.
  roles_expander = RolesExpander(db.roles, realms_cfg.custom_roles)
  # A helper to traverse the realms graph.
  realms_expander = RealmsExpander(roles_expander, conds_set, realms_map)

  # Visit all realms and build preliminary bindings as pairs of
  # (a tuple with permission indexes, a list of principals who have them). The
  # bindings are preliminary since we don't know final permission indexes yet
  # and instead use some internal indexes as generated by RolesExpander. We
  # need to finish this first pass to gather the list of ALL used permissions,
  # so we can calculate final indexes. This is done inside of `roles_expander`.
  realms = []  # [(name, {(permissions tuple, conditions tuple) => [principal]}]
  for name, _ in realms_list:
    # Build a mapping from a principal+conditions to the permissions set.
    #
    # Each map entry `(principal, tuple(conds)) => set(perms)` means `principal`
    # is granted the given set of permissions if all given conditions allow it.
    #
    # This step essentially deduplicates permission bindings that result from
    # expanding realms and roles inheritance chains.
    principal_to_perms = collections.defaultdict(set)
    for principal, perms, conds in realms_expander.per_principal_bindings(name):
      principal_to_perms[(principal, conds)].update(perms)

    # Combine entries with the same set of permissions+conditions into one.
    #
    # Each map entry `(tuple(perms), tuple(conds)) => list(principal)` means
    # all `principals` are granted all given permissions if all given conditions
    # allow it.
    #
    # This step merges principal sets of identical bindings to have a more
    # compact final representation.
    perms_to_principals = collections.defaultdict(list)
    for (principal, conds), perms in principal_to_perms.items():
      perms_norm = tuple(sorted(perms))
      perms_to_principals[(perms_norm, conds)].append(principal)

    # perms_to_principals is essentially a set of all binding in a realm.
    realms.append((name, perms_to_principals))

  # We now know all permissions ever used by all realms. Convert them into the
  # form suitable for realm_pb2 by sorting alphabetically. Keep the mapping
  # between old and new indexes, to be able to change indexes in permission
  # tuples we stored in `realms`.
  perms, index_map = roles_expander.sorted_permissions()

  # Build the final sorted form of all realms by relabeling permissions
  # according to the index_map and by sorting stuff.
  return realms_pb2.Realms(
      permissions=[realms_pb2.Permission(name=p) for p in perms],
      conditions=all_conditions,
      realms=[
          realms_pb2.Realm(
              name='%s:%s' % (project_id, name),
              bindings=to_normalized_bindings(perms_to_principals, index_map),
              data=realms_expander.realm_data(name),
          )
          for name, perms_to_principals in realms
      ])


class RolesExpander(object):
  """Keeps track of permissions and `role => [permission]` expansions.

  Permissions are represented internally as integers to speed up set operations.
  The mapping from a permission to a corresponding integer is lazily built and
  should be considered arbitrary (it depends on the order of method calls). But
  it doesn't matter since in the end we relabel all permissions according to
  their indexes in the final sorted list of permissions.

  Should be used only with validated realms_config_pb2.RealmsCfg, may cause
  stack overflow or raise random exceptions otherwise.
  """

  def __init__(self, builtin_roles, custom_roles):
    self._builtin_roles = builtin_roles
    self._custom_roles = {r.name: r for r in custom_roles}
    self._permissions = {}  # permission name => its index
    self._roles = {}  # role name => set indexes of permissions

  def _perm_index(self, name):
    """Returns an internal index that represents the given permission string."""
    idx = self._permissions.get(name)
    if idx is None:
      idx = len(self._permissions)
      self._permissions[name] = idx
    return idx

  def _perm_indexes(self, iterable):
    """Yields indexes of given permission strings."""
    return (self._perm_index(p) for p in iterable)

  def role(self, role):
    """Returns an unsorted tuple of indexes of permissions of the role."""
    perms = self._roles.get(role)
    if perms is not None:
      return perms

    if role.startswith(permissions.BUILTIN_ROLE_PREFIX):
      perms = self._perm_indexes(self._builtin_roles[role].permissions)
    elif role.startswith(permissions.CUSTOM_ROLE_PREFIX):
      custom_role = self._custom_roles[role]
      perms = set(self._perm_indexes(custom_role.permissions))
      for parent in custom_role.extends:
        perms.update(self.role(parent))
    else:
      raise AssertionError('Impossible role %s' % (role,))

    perms = tuple(perms)
    self._roles[role] = perms
    return perms

  def sorted_permissions(self):
    """Returns a sorted list of permission and a old->new index mapping list.

    See to_normalized_bindings below for how it is used.
    """
    perms = sorted(self._permissions)
    mapping = [None]*len(perms)
    for new_idx, p in enumerate(perms):
      old_idx = self._permissions[p]
      mapping[old_idx] = new_idx
    assert all(v is not None for v in mapping), mapping
    return perms, mapping


class ConditionsSet(object):
  """Normalizes and dedups conditions, maps them to integers.

  Assumes all incoming realms_config_pb2.Condition are immutable and dedups
  them by *identity* (using id(...) function), as well as by normalized values.
  Also assumes the set of all possible *objects* ever passed to indexes(...) was
  also passed to add_condition(...) first (so it could build id => index map).

  This makes hot indexes(...) function fast by allowing to lookup ids instead
  of (potentially huge) protobuf message values.
  """

  def __init__(self):
    # A mapping from a serialized normalized realms_pb2.Condition to a pair
    # (normalized realms_pb2.Condition, its unique index).
    self._normalized = {}
    # A mapping from id(realms_config_pb2.Condition) to its matching index.
    self._mapping = {}
    # A list of all different objects ever passed to add_condition, to retain
    # pointers to them to make sure their id(...)s are not reallocated by Python
    # to point to other objects.
    self._retain = []
    # True if finalize() was already called.
    self._finalized = False

  def add_condition(self, cond):
    """Adds realms_config_pb2.Condition to the set if not already there."""
    assert not self._finalized
    assert isinstance(cond, realms_config_pb2.Condition), cond

    # Check if we already processed this exact object before.
    if id(cond) in self._mapping:
      return

    # Normalize realms_config_pb2.Condition into a realms_pb2.Condition.
    norm = realms_pb2.Condition()
    if cond.HasField('restrict'):
      norm.restrict.attribute = cond.restrict.attribute
      norm.restrict.values.extend(sorted(set(cond.restrict.values)))
    else:
      # Note: this should not be happening, we validated all inputs already.
      raise ValueError('Invalid empty condition %r' % cond)

    # Get a key for the dictionary, since `norm` itself is unhashable and can't
    # be used as a key.
    key = norm.SerializeToString()

    # Append it to the set of unique conditions if not already there.
    idx = self._normalized.setdefault(key, (norm, len(self._normalized)))[1]

    # Remember that we mapped this particular `cond` *object* to this index.
    self._mapping[id(cond)] = idx
    self._retain.append(cond)

  def finalize(self):
    """Finalizes the set preventing any future add_condition(...) calls.

    Sorts the list of stored conditions according to some stable order and
    returns the final sorted list of realms_pb2.Condition. Indexes returned by
    indexes(...) will refer to indexes in this list.
    """
    assert not self._finalized
    self._finalized = True

    # Sort according to their binary representations. The order doesn't matter
    # as long as it is reproducible.
    conds = [
        val for _, val in
        sorted(self._normalized.items(), key=lambda (key, _): key)
    ]
    self._normalized = None   # won't need it anymore

    # Here `conds` is a list of pairs (cond, its old index). We'll need
    # to change self._mapping to use new indexes (matching the new order in
    # `conds`). Build the remapping dict {old index => new index}.
    old_to_new = {old: new for new, (_, old) in enumerate(conds)}
    assert len(old_to_new) == len(conds)

    # Change indexes in _mapping to use the new order.
    for key, old in self._mapping.items():
      self._mapping[key] = old_to_new[old]

    # Return the final list of conditions in the new order.
    return [cond for cond, _ in conds]

  def indexes(self, conds):
    """Given a list of realms_config_pb2.Condition returns a sorted index tuple.

    Can be called only after finalize(). All given conditions must have
    previously been but into the set via add_condition(...). The returned tuple
    can have fewer elements if some conditions in `conds` are equivalent.

    The returned tuple is essentially a compact encoding of the overall AND
    condition expression in a binding.
    """
    assert self._finalized
    # Skip function calls for two most common cases.
    if not conds:
      return ()
    if len(conds) == 1:
      return (self._mapping[id(conds[0])],)
    return tuple(sorted(set(self._mapping[id(cond)] for cond in conds)))


class RealmsExpander(object):
  """Helper to traverse the realm inheritance graph."""

  def __init__(self, roles, conds_set, realms_map):
    self._roles = roles
    self._conds_set = conds_set
    self._realms = realms_map  # name -> realms_config_pb2.Realm
    self._data = {}  # name -> realms_pb2.RealmData, memoized

  @staticmethod
  def _parents(realm):
    """Given a realms_config_pb2.Realm yields names of immediate parents."""
    if realm.name == common.ROOT_REALM:
      return
    yield common.ROOT_REALM
    for name in realm.extends:
      if name != common.ROOT_REALM:
        yield name

  def per_principal_bindings(self, realm):
    """Yields tuples (a single principal, permissions tuple, conditions tuple).

    Visits all bindings in the realm and its parent realms. Returns a lot of
    duplicates. It's the caller's job to skip them.
    """
    r = self._realms[realm]
    assert r.name == realm

    for b in r.bindings:
      perms = self._roles.role(b.role)  # the tuple of permissions of the role
      conds = self._conds_set.indexes(b.conditions)  # the tuple with conditions
      for principal in b.principals:
        yield principal, perms, conds

    for parent in self._parents(r):
      for principal, perms, conds in self.per_principal_bindings(parent):
        yield principal, perms, conds

  def realm_data(self, name):
    """Returns calculated realms_pb2.RealmData for a realm."""
    if name not in self._data:
      realm = self._realms[name]
      extends = [self.realm_data(p) for p in self._parents(realm)]
      self._data[name] = derive_realm_data(realm, [x for x in extends if x])
    return self._data[name]


def to_realms_map(realms_cfg, implicit_root_bindings):
  """Returns a map {realm name => realms_config_pb2.Realm}.

  Makes sure the @root realm is defined there, adding it if necessary.
  Appends the given list of bindings to the root realm.

  Args:
    realms_cfg: the original realms_config_pb2.Realms message.
    implicit_root_bindings: a list of realms_config_pb2.Binding to add to @root.
  """
  realms = {r.name: r for r in realms_cfg.realms}
  root = realms_config_pb2.Realm(name=common.ROOT_REALM)
  if common.ROOT_REALM in realms:
    root.CopyFrom(realms[common.ROOT_REALM])
  root.bindings.extend(implicit_root_bindings)
  realms[common.ROOT_REALM] = root
  return realms


def to_normalized_bindings(perms_to_principals, index_map):
  """Produces a sorted list of realms_pb2.Binding.

  Bindings are given as a map from (permission tuple, conditions tuple) to
  a list of principals that should have all given permission if all given
  conditions allow.

  Permissions are specified through their internal indexes as produced by
  RolesExpander. We convert them into "public" ones (the ones that correspond
  to the sorted permissions list in the realms_pb2.Realms proto). The mapping
  from an old to a new index is given by `new = index_map[old]`.

  Conditions are specified as indexes in ConditionsSet, we use them as they are,
  since by construction of ConditionsSet, all conditions are in use and we don't
  need any extra filtering (and consequently index remapping to skip gaps) as we
  do for permissions.

  Args:
    perms_to_principals: {(permissions tuple, conditions tuple) => [principal]}.
    index_map: defines how to remap permission indexes (old -> new).

  Returns:
    A sorted list of realm_pb2.Binding.
  """
  normalized = (
      (sorted(index_map[idx] for idx in perms), conds, sorted(principals))
      for (perms, conds), principals in perms_to_principals.items()
  )
  return [
      realms_pb2.Binding(
          permissions=perms,
          principals=principals,
          conditions=conds)
      for perms, conds, principals in sorted(normalized)
  ]


def derive_realm_data(realm, extends):
  """Calculates realms_pb2.RealmData from the realm config and parent data.

  Args:
    realm: realms_config_pb2.Realm to calculate the data for.
    extends: a list of realms_pb2.RealmData it extends from.

  Returns:
    realms_pb2.RealmData or None if empty.
  """
  enforce_in_service = set(realm.enforce_in_service)
  for d in extends:
    enforce_in_service.update(d.enforce_in_service)
  if not enforce_in_service:
    return None
  return realms_pb2.RealmData(enforce_in_service=sorted(enforce_in_service))
