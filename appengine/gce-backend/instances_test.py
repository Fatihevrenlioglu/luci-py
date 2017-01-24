#!/usr/bin/python
# Copyright 2016 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

"""Unit tests for instances.py."""

import unittest

import test_env
test_env.setup_test_env()

from google.appengine.ext import ndb

from components import datastore_utils
from test_support import test_case

import instance_group_managers
import instances
import models


class GetInstanceGroupManagerKey(test_case.TestCase):
  """Tests for instances.get_instance_group_manager_key."""

  def test_equal(self):
    expected = instance_group_managers.get_instance_group_manager_key(
        'base-name',
        'revision',
        'zone',
    )

    key = instances.get_instance_key(
        'base-name',
        'revision',
        'zone',
        'instance-name',
    )

    self.assertEqual(instances.get_instance_group_manager_key(key), expected)


class EnsureEntityExistsTest(test_case.TestCase):
  """Tests for instances.ensure_entity_exists."""

  def test_creates(self):
    """Ensures entity is created when it doesn't exist."""
    def send_machine_event(*args, **kwargs):
      pass
    self.mock(instances.metrics, 'send_machine_event', send_machine_event)

    key = instances.get_instance_key(
        'base-name',
        'revision',
        'zone',
        'instance-name',
    )
    expected_url = 'url'

    future = instances.ensure_entity_exists(
        key,
        expected_url,
        instances.get_instance_group_manager_key(key),
    )
    future.wait()

    self.assertEqual(key.get().url, expected_url)

  def test_entity_exists(self):
    """Ensures nothing happens when the entity already exists."""
    key = models.Instance(
        key=instances.get_instance_key(
            'base-name',
            'revision',
            'zone',
            'instance-name',
        ),
    ).put()

    future = instances.ensure_entity_exists(
        key, 'url', instances.get_instance_group_manager_key(key))
    future.wait()

    self.failIf(key.get().url)


class EnsureEntitiesExistTest(test_case.TestCase):
  """Tests for instances.ensure_entities_exist."""

  def test_entity_doesnt_exist(self):
    """Ensures nothing happens when the entity doesn't exist."""
    key = ndb.Key(models.InstanceGroupManager, 'fake-key')

    instances.ensure_entities_exist(key)
    self.failIf(key.get())

  def test_url_unspecified(self):
    """Ensures nothing happens when URL is unspecified."""
    key = models.InstanceGroupManager(
        key=instance_group_managers.get_instance_group_manager_key(
            'base-name',
            'revision',
            'zone',
        ),
    ).put()

    instances.ensure_entities_exist(key)
    self.failIf(key.get().instances)

  def test_no_instances(self):
    """Ensures nothing happens when there are no instances."""
    def fetch(*args, **kwargs):
      return []
    self.mock(instances, 'fetch', fetch)

    key = models.InstanceGroupManager(
        key=instance_group_managers.get_instance_group_manager_key(
            'base-name',
            'revision',
            'zone',
        ),
        url='url',
    ).put()

    instances.ensure_entities_exist(key)
    self.failIf(key.get().instances)

  def test_already_exists(self):
    """Ensures nothing happens when the entity already exists."""
    def fetch(*args, **kwargs):
      return ['url/name']
    self.mock(instances, 'fetch', fetch)

    key = instances.get_instance_key(
        'base-name',
        'revision',
        'zone',
        'name',
    )
    models.Instance(
        key=key,
        instance_group_manager=instances.get_instance_group_manager_key(key),
    ).put()
    models.InstanceGroupManager(
        key=instances.get_instance_group_manager_key(key),
        url='url',
    ).put()
    expected_instances = [
        key,
    ]

    instances.ensure_entities_exist(
        instances.get_instance_group_manager_key(key))
    self.failIf(key.get().url)
    self.assertItemsEqual(
        instances.get_instance_group_manager_key(key).get().instances,
        expected_instances,
    )

  def test_creates(self):
    """Ensures entity gets created."""
    def fetch(*args, **kwargs):
      return ['url/name']
    def send_machine_event(*args, **kwargs):
      pass
    self.mock(instances, 'fetch', fetch)
    self.mock(instances.metrics, 'send_machine_event', send_machine_event)

    key = instances.get_instance_key(
        'base-name',
        'revision',
        'zone',
        'name',
    )
    models.InstanceGroupManager(
        key=instances.get_instance_group_manager_key(key),
        url='url',
    ).put()
    expected_instances = [
        key,
    ]
    expected_url = 'url/name'

    instances.ensure_entities_exist(
        instances.get_instance_group_manager_key(key))
    self.assertItemsEqual(
        instances.get_instance_group_manager_key(key).get().instances,
        expected_instances,
    )
    self.assertEqual(key.get().url, expected_url)


class FetchTest(test_case.TestCase):
  """Tests for instances.fetch."""

  def test_entity_doesnt_exist(self):
    """Ensures nothing happens when the entity doesn't exist."""
    key = ndb.Key(models.InstanceGroupManager, 'fake-key')
    urls = instances.fetch(key)
    self.failIf(urls)

  def test_url_unspecified(self):
    """Ensures nothing happens when URL is unspecified."""
    key = models.InstanceGroupManager(
        key=instance_group_managers.get_instance_group_manager_key(
            'base-name',
            'revision',
            'zone',
        ),
    ).put()
    models.InstanceTemplateRevision(key=key.parent(), project='project').put()

    urls = instances.fetch(key)
    self.failIf(urls)

  def test_parent_doesnt_exist(self):
    """Ensures nothing happens when the parent doesn't exist."""
    key = models.InstanceGroupManager(
        key=instance_group_managers.get_instance_group_manager_key(
            'base-name',
            'revision',
            'zone',
        ),
    ).put()

    urls = instances.fetch(key)
    self.failIf(urls)

  def test_parent_project_unspecified(self):
    """Ensures nothing happens when parent doesn't specify a project."""
    key = models.InstanceGroupManager(
        key=instance_group_managers.get_instance_group_manager_key(
            'base-name',
            'revision',
            'zone',
        ),
    ).put()
    models.InstanceTemplateRevision(key=key.parent()).put()

    urls = instances.fetch(key)
    self.failIf(urls)

  def test_no_instances(self):
    """Ensures nothing happens when there are no instances."""
    def get_instances_in_instance_group(*args, **kwargs):
      return {}
    self.mock(
        instances.gce.Project,
        'get_instances_in_instance_group',
        get_instances_in_instance_group,
    )

    key = models.InstanceGroupManager(
        key=instance_group_managers.get_instance_group_manager_key(
            'base-name',
            'revision',
            'zone',
        ),
        url='url',
    ).put()
    models.InstanceTemplateRevision(key=key.parent(), project='project').put()

    urls = instances.fetch(key)
    self.failIf(urls)

  def test_instances(self):
    """Ensures instances are returned."""
    def get_instances_in_instance_group(*args, **kwargs):
      return {
          'instanceGroup': 'instance-group-url',
          'items': [
              {'instance': 'url/instance'},
          ],
      }
    self.mock(
        instances.gce.Project,
        'get_instances_in_instance_group',
        get_instances_in_instance_group,
    )

    key = models.InstanceGroupManager(
        key=instance_group_managers.get_instance_group_manager_key(
            'base-name',
            'revision',
            'zone',
        ),
        url='url',
    ).put()
    models.InstanceTemplateRevision(key=key.parent(), project='project').put()
    expected_urls = ['url/instance']

    urls = instances.fetch(key)
    self.assertItemsEqual(urls, expected_urls)

  def test_instances_with_page_token(self):
    """Ensures all instances are returned."""
    def get_instances_in_instance_group(*args, **kwargs):
      if kwargs.get('page_token'):
        return {
            'items': [
                {'instance': 'url/instance-2'},
            ],
        }
      return {
          'items': [
              {'instance': 'url/instance-1'},
          ],
          'nextPageToken': 'page-token',
      }
    self.mock(
        instances.gce.Project,
        'get_instances_in_instance_group',
        get_instances_in_instance_group,
    )

    key = models.InstanceGroupManager(
        key=instance_group_managers.get_instance_group_manager_key(
            'base-name',
            'revision',
            'zone',
        ),
        url='url',
    ).put()
    models.InstanceTemplateRevision(key=key.parent(), project='project').put()
    expected_urls = ['url/instance-1', 'url/instance-2']

    urls = instances.fetch(key)
    self.assertItemsEqual(urls, expected_urls)


if __name__ == '__main__':
  unittest.main()
