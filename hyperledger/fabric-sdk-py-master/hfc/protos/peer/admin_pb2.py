# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/peer/admin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/peer/admin.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x1bhfc/protos/peer/admin.proto\x12\x06protos\x1a\x1bgoogle/protobuf/empty.proto\"\x9a\x01\n\x0cServerStatus\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.protos.ServerStatus.StatusCode\"Y\n\nStatusCode\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\x0b\n\x07STOPPED\x10\x02\x12\n\n\x06PAUSED\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x12\x0b\n\x07UNKNOWN\x10\x05\"8\n\x0fLogLevelRequest\x12\x12\n\nlog_module\x18\x01 \x01(\t\x12\x11\n\tlog_level\x18\x02 \x01(\t\"9\n\x10LogLevelResponse\x12\x12\n\nlog_module\x18\x01 \x01(\t\x12\x11\n\tlog_level\x18\x02 \x01(\t2\xdc\x02\n\x05\x41\x64min\x12;\n\tGetStatus\x12\x16.google.protobuf.Empty\x1a\x14.protos.ServerStatus\"\x00\x12=\n\x0bStartServer\x12\x16.google.protobuf.Empty\x1a\x14.protos.ServerStatus\"\x00\x12H\n\x11GetModuleLogLevel\x12\x17.protos.LogLevelRequest\x1a\x18.protos.LogLevelResponse\"\x00\x12H\n\x11SetModuleLogLevel\x12\x17.protos.LogLevelRequest\x1a\x18.protos.LogLevelResponse\"\x00\x12\x43\n\x0fRevertLogLevels\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x42]\n\"org.hyperledger.fabric.protos.peerB\x0c\x41\x64minPackageZ)github.com/hyperledger/fabric/protos/peerb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])



_SERVERSTATUS_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='protos.ServerStatus.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARTED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=134,
  serialized_end=223,
)
_sym_db.RegisterEnumDescriptor(_SERVERSTATUS_STATUSCODE)


_SERVERSTATUS = _descriptor.Descriptor(
  name='ServerStatus',
  full_name='protos.ServerStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='protos.ServerStatus.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERSTATUS_STATUSCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=223,
)


_LOGLEVELREQUEST = _descriptor.Descriptor(
  name='LogLevelRequest',
  full_name='protos.LogLevelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_module', full_name='protos.LogLevelRequest.log_module', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_level', full_name='protos.LogLevelRequest.log_level', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=281,
)


_LOGLEVELRESPONSE = _descriptor.Descriptor(
  name='LogLevelResponse',
  full_name='protos.LogLevelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_module', full_name='protos.LogLevelResponse.log_module', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_level', full_name='protos.LogLevelResponse.log_level', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=340,
)

_SERVERSTATUS.fields_by_name['status'].enum_type = _SERVERSTATUS_STATUSCODE
_SERVERSTATUS_STATUSCODE.containing_type = _SERVERSTATUS
DESCRIPTOR.message_types_by_name['ServerStatus'] = _SERVERSTATUS
DESCRIPTOR.message_types_by_name['LogLevelRequest'] = _LOGLEVELREQUEST
DESCRIPTOR.message_types_by_name['LogLevelResponse'] = _LOGLEVELRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerStatus = _reflection.GeneratedProtocolMessageType('ServerStatus', (_message.Message,), dict(
  DESCRIPTOR = _SERVERSTATUS,
  __module__ = 'hfc.protos.peer.admin_pb2'
  # @@protoc_insertion_point(class_scope:protos.ServerStatus)
  ))
_sym_db.RegisterMessage(ServerStatus)

LogLevelRequest = _reflection.GeneratedProtocolMessageType('LogLevelRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGLEVELREQUEST,
  __module__ = 'hfc.protos.peer.admin_pb2'
  # @@protoc_insertion_point(class_scope:protos.LogLevelRequest)
  ))
_sym_db.RegisterMessage(LogLevelRequest)

LogLevelResponse = _reflection.GeneratedProtocolMessageType('LogLevelResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOGLEVELRESPONSE,
  __module__ = 'hfc.protos.peer.admin_pb2'
  # @@protoc_insertion_point(class_scope:protos.LogLevelResponse)
  ))
_sym_db.RegisterMessage(LogLevelResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"org.hyperledger.fabric.protos.peerB\014AdminPackageZ)github.com/hyperledger/fabric/protos/peer'))

_ADMIN = _descriptor.ServiceDescriptor(
  name='Admin',
  full_name='protos.Admin',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=343,
  serialized_end=691,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetStatus',
    full_name='protos.Admin.GetStatus',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_SERVERSTATUS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartServer',
    full_name='protos.Admin.StartServer',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_SERVERSTATUS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetModuleLogLevel',
    full_name='protos.Admin.GetModuleLogLevel',
    index=2,
    containing_service=None,
    input_type=_LOGLEVELREQUEST,
    output_type=_LOGLEVELRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetModuleLogLevel',
    full_name='protos.Admin.SetModuleLogLevel',
    index=3,
    containing_service=None,
    input_type=_LOGLEVELREQUEST,
    output_type=_LOGLEVELRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RevertLogLevels',
    full_name='protos.Admin.RevertLogLevels',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADMIN)

DESCRIPTOR.services_by_name['Admin'] = _ADMIN

# @@protoc_insertion_point(module_scope)
