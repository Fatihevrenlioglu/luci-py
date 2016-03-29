# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='gce_backend',
  serialized_pb='\n\x0c\x63onfig.proto\x12\x0bgce_backend\"\x87\x03\n\x16InstanceTemplateConfig\x12G\n\ttemplates\x18\x01 \x03(\x0b\x32\x34.gce_backend.InstanceTemplateConfig.InstanceTemplate\x1a\xa3\x02\n\x10InstanceTemplate\x12\x11\n\tbase_name\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x12\n\ndimensions\x18\x03 \x03(\t\x12\x12\n\nimage_name\x18\x04 \x01(\t\x12\x14\n\x0c\x64isk_size_gb\x18\x05 \x01(\x05\x12]\n\x10service_accounts\x18\x06 \x03(\x0b\x32\x43.gce_backend.InstanceTemplateConfig.InstanceTemplate.ServiceAccount\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12\x10\n\x08metadata\x18\x08 \x03(\t\x1a.\n\x0eServiceAccount\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06scopes\x18\x02 \x03(\t\"\xcc\x01\n\x1aInstanceGroupManagerConfig\x12N\n\x08managers\x18\x01 \x03(\x0b\x32<.gce_backend.InstanceGroupManagerConfig.InstanceGroupManager\x1a^\n\x14InstanceGroupManager\x12\x1a\n\x12template_base_name\x18\x01 \x01(\t\x12\x14\n\x0cminimum_size\x18\x02 \x01(\x05\x12\x14\n\x0cmaximum_size\x18\x03 \x01(\x05')




_INSTANCETEMPLATECONFIG_INSTANCETEMPLATE_SERVICEACCOUNT = _descriptor.Descriptor(
  name='ServiceAccount',
  full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate.ServiceAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate.ServiceAccount.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scopes', full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate.ServiceAccount.scopes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=375,
  serialized_end=421,
)

_INSTANCETEMPLATECONFIG_INSTANCETEMPLATE = _descriptor.Descriptor(
  name='InstanceTemplate',
  full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_name', full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate.base_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='project', full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate.project', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate.dimensions', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_name', full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate.image_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disk_size_gb', full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate.disk_size_gb', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service_accounts', full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate.service_accounts', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate.tags', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='gce_backend.InstanceTemplateConfig.InstanceTemplate.metadata', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_INSTANCETEMPLATECONFIG_INSTANCETEMPLATE_SERVICEACCOUNT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=130,
  serialized_end=421,
)

_INSTANCETEMPLATECONFIG = _descriptor.Descriptor(
  name='InstanceTemplateConfig',
  full_name='gce_backend.InstanceTemplateConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='templates', full_name='gce_backend.InstanceTemplateConfig.templates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_INSTANCETEMPLATECONFIG_INSTANCETEMPLATE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=30,
  serialized_end=421,
)


_INSTANCEGROUPMANAGERCONFIG_INSTANCEGROUPMANAGER = _descriptor.Descriptor(
  name='InstanceGroupManager',
  full_name='gce_backend.InstanceGroupManagerConfig.InstanceGroupManager',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_base_name', full_name='gce_backend.InstanceGroupManagerConfig.InstanceGroupManager.template_base_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum_size', full_name='gce_backend.InstanceGroupManagerConfig.InstanceGroupManager.minimum_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maximum_size', full_name='gce_backend.InstanceGroupManagerConfig.InstanceGroupManager.maximum_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=534,
  serialized_end=628,
)

_INSTANCEGROUPMANAGERCONFIG = _descriptor.Descriptor(
  name='InstanceGroupManagerConfig',
  full_name='gce_backend.InstanceGroupManagerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='managers', full_name='gce_backend.InstanceGroupManagerConfig.managers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_INSTANCEGROUPMANAGERCONFIG_INSTANCEGROUPMANAGER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=424,
  serialized_end=628,
)

_INSTANCETEMPLATECONFIG_INSTANCETEMPLATE_SERVICEACCOUNT.containing_type = _INSTANCETEMPLATECONFIG_INSTANCETEMPLATE;
_INSTANCETEMPLATECONFIG_INSTANCETEMPLATE.fields_by_name['service_accounts'].message_type = _INSTANCETEMPLATECONFIG_INSTANCETEMPLATE_SERVICEACCOUNT
_INSTANCETEMPLATECONFIG_INSTANCETEMPLATE.containing_type = _INSTANCETEMPLATECONFIG;
_INSTANCETEMPLATECONFIG.fields_by_name['templates'].message_type = _INSTANCETEMPLATECONFIG_INSTANCETEMPLATE
_INSTANCEGROUPMANAGERCONFIG_INSTANCEGROUPMANAGER.containing_type = _INSTANCEGROUPMANAGERCONFIG;
_INSTANCEGROUPMANAGERCONFIG.fields_by_name['managers'].message_type = _INSTANCEGROUPMANAGERCONFIG_INSTANCEGROUPMANAGER
DESCRIPTOR.message_types_by_name['InstanceTemplateConfig'] = _INSTANCETEMPLATECONFIG
DESCRIPTOR.message_types_by_name['InstanceGroupManagerConfig'] = _INSTANCEGROUPMANAGERCONFIG

class InstanceTemplateConfig(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class InstanceTemplate(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType

    class ServiceAccount(_message.Message):
      __metaclass__ = _reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _INSTANCETEMPLATECONFIG_INSTANCETEMPLATE_SERVICEACCOUNT

      # @@protoc_insertion_point(class_scope:gce_backend.InstanceTemplateConfig.InstanceTemplate.ServiceAccount)
    DESCRIPTOR = _INSTANCETEMPLATECONFIG_INSTANCETEMPLATE

    # @@protoc_insertion_point(class_scope:gce_backend.InstanceTemplateConfig.InstanceTemplate)
  DESCRIPTOR = _INSTANCETEMPLATECONFIG

  # @@protoc_insertion_point(class_scope:gce_backend.InstanceTemplateConfig)

class InstanceGroupManagerConfig(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class InstanceGroupManager(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _INSTANCEGROUPMANAGERCONFIG_INSTANCEGROUPMANAGER

    # @@protoc_insertion_point(class_scope:gce_backend.InstanceGroupManagerConfig.InstanceGroupManager)
  DESCRIPTOR = _INSTANCEGROUPMANAGERCONFIG

  # @@protoc_insertion_point(class_scope:gce_backend.InstanceGroupManagerConfig)


# @@protoc_insertion_point(module_scope)
