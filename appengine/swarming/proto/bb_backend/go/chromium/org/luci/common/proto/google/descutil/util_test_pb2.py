# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/bb_backend/go.chromium.org/luci/common/proto/google/descutil/util_test.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/bb_backend/go.chromium.org/luci/common/proto/google/descutil/util_test.proto',
  package='descutil',
  syntax='proto3',
  serialized_options=b'Z:go.chromium.org/luci/common/proto/google/descutil;descutil',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nRproto/bb_backend/go.chromium.org/luci/common/proto/google/descutil/util_test.proto\x12\x08\x64\x65scutil\x1a google/protobuf/descriptor.proto\" \n\x08SuperExt\x12\t\n\x01\x61\x18\x01 \x01(\t\x12\t\n\x01\x62\x18\x02 \x01(\t\"x\n\x02M1\x12$\n\x02\x66\x31\x18\x01 \x01(\tB\x12\x8a\xb5\x18\x04narf\x92\xb5\x18\x06\n\x01\x61\x12\x01\x62R\x04\x66oof\x12\x12\n\x04meep\x18\x02 \x03(\x03\x42\x04\x10\x00\x30\x02\x12\x1a\n\x12regular_snake_case\x18\x03 \x01(\x08\x12\x1c\n\x0eonly_json_name\x18\x04 \x01(\x08R\x04\x63ool\"T\n\x02M2\x12\x18\n\x02\x66\x31\x18\x01 \x03(\x0b\x32\x0c.descutil.M1\x12\x18\n\x02\x66\x32\x18\x02 \x01(\x0e\x32\x0c.descutil.E1:\x1a\x18\x01\x8a\xb5\x18\x03yep\x92\xb5\x18\r\n\x04\x63ool\x12\x05\x62\x65\x61ns\"`\n\x02M3\x12\x0c\n\x02\x66\x31\x18\x01 \x01(\x05H\x00\x12\x0c\n\x02\x66\x32\x18\x02 \x01(\x05H\x00\x12\x0c\n\x02\x66\x33\x18\x03 \x01(\x05H\x01\x12\x0c\n\x02\x66\x34\x18\x04 \x01(\x05H\x01\x12\n\n\x02\x66\x35\x18\x05 \x01(\t\x12\n\n\x02\x66\x36\x18\x06 \x01(\x05\x42\x04\n\x02O1B\x04\n\x02O2\"\\\n\x13NestedMessageParent\x1a\'\n\rNestedMessage\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12\n\n\x02\x66\x32\x18\x02 \x01(\x05\"\x1c\n\nNestedEnum\x12\x06\n\x02V0\x10\x00\x12\x06\n\x02V1\x10\x01\"2\n\x16ReservedRangeContainerJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03R\x05helloR\x05world*\x14\n\x02\x45\x31\x12\x06\n\x02V0\x10\x00\x12\x06\n\x02V1\x10\x01\x32(\n\x02S1\x12\"\n\x02R1\x12\x0c.descutil.M1\x1a\x0c.descutil.M2\"\x00\x32L\n\x02S2\x12\"\n\x02R1\x12\x0c.descutil.M1\x1a\x0c.descutil.M2\"\x00\x12\"\n\x02R2\x12\x0c.descutil.M1\x1a\x0c.descutil.M2\"\x00:,\n\x03\x65xt\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\t:F\n\tsuper_ext\x12\x1d.google.protobuf.FieldOptions\x18\xd2\x86\x03 \x01(\x0b\x32\x12.descutil.SuperExt:1\n\x06msgExt\x12\x1f.google.protobuf.MessageOptions\x18\xd1\x86\x03 \x01(\t:L\n\rsuper_msg_ext\x12\x1f.google.protobuf.MessageOptions\x18\xd2\x86\x03 \x01(\x0b\x32\x12.descutil.SuperExtB<Z:go.chromium.org/luci/common/proto/google/descutil;descutilb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_E1 = _descriptor.EnumDescriptor(
  name='E1',
  full_name='descutil.E1',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='V0', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=616,
  serialized_end=636,
)
_sym_db.RegisterEnumDescriptor(_E1)

E1 = enum_type_wrapper.EnumTypeWrapper(_E1)
V0 = 0
V1 = 1

EXT_FIELD_NUMBER = 50001
ext = _descriptor.FieldDescriptor(
  name='ext', full_name='descutil.ext', index=0,
  number=50001, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
SUPER_EXT_FIELD_NUMBER = 50002
super_ext = _descriptor.FieldDescriptor(
  name='super_ext', full_name='descutil.super_ext', index=1,
  number=50002, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
MSGEXT_FIELD_NUMBER = 50001
msgExt = _descriptor.FieldDescriptor(
  name='msgExt', full_name='descutil.msgExt', index=2,
  number=50001, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
SUPER_MSG_EXT_FIELD_NUMBER = 50002
super_msg_ext = _descriptor.FieldDescriptor(
  name='super_msg_ext', full_name='descutil.super_msg_ext', index=3,
  number=50002, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

_NESTEDMESSAGEPARENT_NESTEDENUM = _descriptor.EnumDescriptor(
  name='NestedEnum',
  full_name='descutil.NestedMessageParent.NestedEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='V0', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=534,
  serialized_end=562,
)
_sym_db.RegisterEnumDescriptor(_NESTEDMESSAGEPARENT_NESTEDENUM)


_SUPEREXT = _descriptor.Descriptor(
  name='SuperExt',
  full_name='descutil.SuperExt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='descutil.SuperExt.a', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='descutil.SuperExt.b', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=162,
)


_M1 = _descriptor.Descriptor(
  name='M1',
  full_name='descutil.M1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='descutil.M1.f1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\004narf\222\265\030\006\n\001a\022\001b', json_name='foof', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meep', full_name='descutil.M1.meep', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\0000\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regular_snake_case', full_name='descutil.M1.regular_snake_case', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='only_json_name', full_name='descutil.M1.only_json_name', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='cool', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=284,
)


_M2 = _descriptor.Descriptor(
  name='M2',
  full_name='descutil.M2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='descutil.M2.f1', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f2', full_name='descutil.M2.f2', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\030\001\212\265\030\003yep\222\265\030\r\n\004cool\022\005beans',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=370,
)


_M3 = _descriptor.Descriptor(
  name='M3',
  full_name='descutil.M3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='descutil.M3.f1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f2', full_name='descutil.M3.f2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f3', full_name='descutil.M3.f3', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f4', full_name='descutil.M3.f4', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f5', full_name='descutil.M3.f5', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f6', full_name='descutil.M3.f6', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='O1', full_name='descutil.M3.O1',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='O2', full_name='descutil.M3.O2',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=372,
  serialized_end=468,
)


_NESTEDMESSAGEPARENT_NESTEDMESSAGE = _descriptor.Descriptor(
  name='NestedMessage',
  full_name='descutil.NestedMessageParent.NestedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='descutil.NestedMessageParent.NestedMessage.f1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f2', full_name='descutil.NestedMessageParent.NestedMessage.f2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=532,
)

_NESTEDMESSAGEPARENT = _descriptor.Descriptor(
  name='NestedMessageParent',
  full_name='descutil.NestedMessageParent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_NESTEDMESSAGEPARENT_NESTEDMESSAGE, ],
  enum_types=[
    _NESTEDMESSAGEPARENT_NESTEDENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=562,
)


_RESERVEDRANGECONTAINER = _descriptor.Descriptor(
  name='ReservedRangeContainer',
  full_name='descutil.ReservedRangeContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=564,
  serialized_end=614,
)

_M2.fields_by_name['f1'].message_type = _M1
_M2.fields_by_name['f2'].enum_type = _E1
_M3.oneofs_by_name['O1'].fields.append(
  _M3.fields_by_name['f1'])
_M3.fields_by_name['f1'].containing_oneof = _M3.oneofs_by_name['O1']
_M3.oneofs_by_name['O1'].fields.append(
  _M3.fields_by_name['f2'])
_M3.fields_by_name['f2'].containing_oneof = _M3.oneofs_by_name['O1']
_M3.oneofs_by_name['O2'].fields.append(
  _M3.fields_by_name['f3'])
_M3.fields_by_name['f3'].containing_oneof = _M3.oneofs_by_name['O2']
_M3.oneofs_by_name['O2'].fields.append(
  _M3.fields_by_name['f4'])
_M3.fields_by_name['f4'].containing_oneof = _M3.oneofs_by_name['O2']
_NESTEDMESSAGEPARENT_NESTEDMESSAGE.containing_type = _NESTEDMESSAGEPARENT
_NESTEDMESSAGEPARENT_NESTEDENUM.containing_type = _NESTEDMESSAGEPARENT
DESCRIPTOR.message_types_by_name['SuperExt'] = _SUPEREXT
DESCRIPTOR.message_types_by_name['M1'] = _M1
DESCRIPTOR.message_types_by_name['M2'] = _M2
DESCRIPTOR.message_types_by_name['M3'] = _M3
DESCRIPTOR.message_types_by_name['NestedMessageParent'] = _NESTEDMESSAGEPARENT
DESCRIPTOR.message_types_by_name['ReservedRangeContainer'] = _RESERVEDRANGECONTAINER
DESCRIPTOR.enum_types_by_name['E1'] = _E1
DESCRIPTOR.extensions_by_name['ext'] = ext
DESCRIPTOR.extensions_by_name['super_ext'] = super_ext
DESCRIPTOR.extensions_by_name['msgExt'] = msgExt
DESCRIPTOR.extensions_by_name['super_msg_ext'] = super_msg_ext
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SuperExt = _reflection.GeneratedProtocolMessageType('SuperExt', (_message.Message,), {
  'DESCRIPTOR' : _SUPEREXT,
  '__module__' : 'proto.bb_backend.go.chromium.org.luci.common.proto.google.descutil.util_test_pb2'
  # @@protoc_insertion_point(class_scope:descutil.SuperExt)
  })
_sym_db.RegisterMessage(SuperExt)

M1 = _reflection.GeneratedProtocolMessageType('M1', (_message.Message,), {
  'DESCRIPTOR' : _M1,
  '__module__' : 'proto.bb_backend.go.chromium.org.luci.common.proto.google.descutil.util_test_pb2'
  # @@protoc_insertion_point(class_scope:descutil.M1)
  })
_sym_db.RegisterMessage(M1)

M2 = _reflection.GeneratedProtocolMessageType('M2', (_message.Message,), {
  'DESCRIPTOR' : _M2,
  '__module__' : 'proto.bb_backend.go.chromium.org.luci.common.proto.google.descutil.util_test_pb2'
  # @@protoc_insertion_point(class_scope:descutil.M2)
  })
_sym_db.RegisterMessage(M2)

M3 = _reflection.GeneratedProtocolMessageType('M3', (_message.Message,), {
  'DESCRIPTOR' : _M3,
  '__module__' : 'proto.bb_backend.go.chromium.org.luci.common.proto.google.descutil.util_test_pb2'
  # @@protoc_insertion_point(class_scope:descutil.M3)
  })
_sym_db.RegisterMessage(M3)

NestedMessageParent = _reflection.GeneratedProtocolMessageType('NestedMessageParent', (_message.Message,), {

  'NestedMessage' : _reflection.GeneratedProtocolMessageType('NestedMessage', (_message.Message,), {
    'DESCRIPTOR' : _NESTEDMESSAGEPARENT_NESTEDMESSAGE,
    '__module__' : 'proto.bb_backend.go.chromium.org.luci.common.proto.google.descutil.util_test_pb2'
    # @@protoc_insertion_point(class_scope:descutil.NestedMessageParent.NestedMessage)
    })
  ,
  'DESCRIPTOR' : _NESTEDMESSAGEPARENT,
  '__module__' : 'proto.bb_backend.go.chromium.org.luci.common.proto.google.descutil.util_test_pb2'
  # @@protoc_insertion_point(class_scope:descutil.NestedMessageParent)
  })
_sym_db.RegisterMessage(NestedMessageParent)
_sym_db.RegisterMessage(NestedMessageParent.NestedMessage)

ReservedRangeContainer = _reflection.GeneratedProtocolMessageType('ReservedRangeContainer', (_message.Message,), {
  'DESCRIPTOR' : _RESERVEDRANGECONTAINER,
  '__module__' : 'proto.bb_backend.go.chromium.org.luci.common.proto.google.descutil.util_test_pb2'
  # @@protoc_insertion_point(class_scope:descutil.ReservedRangeContainer)
  })
_sym_db.RegisterMessage(ReservedRangeContainer)

google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(ext)
super_ext.message_type = _SUPEREXT
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(super_ext)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(msgExt)
super_msg_ext.message_type = _SUPEREXT
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(super_msg_ext)

DESCRIPTOR._options = None
_M1.fields_by_name['f1']._options = None
_M1.fields_by_name['meep']._options = None
_M2._options = None

_S1 = _descriptor.ServiceDescriptor(
  name='S1',
  full_name='descutil.S1',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=638,
  serialized_end=678,
  methods=[
  _descriptor.MethodDescriptor(
    name='R1',
    full_name='descutil.S1.R1',
    index=0,
    containing_service=None,
    input_type=_M1,
    output_type=_M2,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_S1)

DESCRIPTOR.services_by_name['S1'] = _S1


_S2 = _descriptor.ServiceDescriptor(
  name='S2',
  full_name='descutil.S2',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=680,
  serialized_end=756,
  methods=[
  _descriptor.MethodDescriptor(
    name='R1',
    full_name='descutil.S2.R1',
    index=0,
    containing_service=None,
    input_type=_M1,
    output_type=_M2,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='R2',
    full_name='descutil.S2.R2',
    index=1,
    containing_service=None,
    input_type=_M1,
    output_type=_M2,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_S2)

DESCRIPTOR.services_by_name['S2'] = _S2

# @@protoc_insertion_point(module_scope)