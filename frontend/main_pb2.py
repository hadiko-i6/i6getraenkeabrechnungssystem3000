# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='main.proto',
  package='i6getraenkeabrechnungssystem3000.rpc',
  syntax='proto3',
  serialized_pb=_b('\n\nmain.proto\x12$i6getraenkeabrechnungssystem3000.rpc\"*\n\x14TerminalStateRequest\x12\x12\n\nTerminalID\x18\x01 \x01(\t\"\xc2\x02\n\x15TerminalStateResponse\x12U\n\x08\x41\x63\x63ounts\x18\x01 \x03(\x0b\x32\x43.i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Account\x12T\n\tOrderList\x18\x02 \x03(\x0b\x32\x41.i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Order\x1a;\n\x07\x41\x63\x63ount\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x13\n\x0b\x44isplayName\x18\x02 \x01(\t\x12\x0f\n\x07\x42\x61lance\x18\x03 \x01(\x11\x1a?\n\x05Order\x12\x13\n\x0b\x44isplayName\x18\x01 \x01(\t\x12\x11\n\tUnitPrice\x18\x02 \x01(\x11\x12\x0e\n\x06\x41mount\x18\x03 \x01(\r\";\n\x12TerminalBuyRequest\x12\x12\n\nTerminalID\x18\x01 \x01(\t\x12\x11\n\tAccountID\x18\x02 \x01(\t\"$\n\x13TerminalBuyResponse\x12\r\n\x05\x45rror\x18\x01 \x01(\t\"<\n\x13TerminalScanRequest\x12\x12\n\nTerminalID\x18\x01 \x01(\t\x12\x11\n\tProductID\x18\x02 \x01(\t\"%\n\x14TerminalScanResponse\x12\r\n\x05\x45rror\x18\x01 \x01(\t\"\"\n\x0c\x41\x62ortRequest\x12\x12\n\nTerminalID\x18\x01 \x01(\t\"\x1e\n\rAbortResponse\x12\r\n\x05\x45rror\x18\x01 \x01(\t2\x8c\x04\n\x0fTerminalBackend\x12\x85\x01\n\x08GetState\x12:.i6getraenkeabrechnungssystem3000.rpc.TerminalStateRequest\x1a;.i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse\"\x00\x12|\n\x03\x42uy\x12\x38.i6getraenkeabrechnungssystem3000.rpc.TerminalBuyRequest\x1a\x39.i6getraenkeabrechnungssystem3000.rpc.TerminalBuyResponse\"\x00\x12\x7f\n\x04Scan\x12\x39.i6getraenkeabrechnungssystem3000.rpc.TerminalScanRequest\x1a:.i6getraenkeabrechnungssystem3000.rpc.TerminalScanResponse\"\x00\x12r\n\x05\x41\x62ort\x12\x32.i6getraenkeabrechnungssystem3000.rpc.AbortRequest\x1a\x33.i6getraenkeabrechnungssystem3000.rpc.AbortResponse\"\x00\x42\x05Z\x03rpcb\x06proto3')
)




_TERMINALSTATEREQUEST = _descriptor.Descriptor(
  name='TerminalStateRequest',
  full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TerminalID', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateRequest.TerminalID', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=52,
  serialized_end=94,
)


_TERMINALSTATERESPONSE_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Account.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DisplayName', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Account.DisplayName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Balance', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Account.Balance', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=295,
  serialized_end=354,
)

_TERMINALSTATERESPONSE_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='DisplayName', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Order.DisplayName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='UnitPrice', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Order.UnitPrice', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Amount', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Order.Amount', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=356,
  serialized_end=419,
)

_TERMINALSTATERESPONSE = _descriptor.Descriptor(
  name='TerminalStateResponse',
  full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Accounts', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='OrderList', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.OrderList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TERMINALSTATERESPONSE_ACCOUNT, _TERMINALSTATERESPONSE_ORDER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=419,
)


_TERMINALBUYREQUEST = _descriptor.Descriptor(
  name='TerminalBuyRequest',
  full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalBuyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TerminalID', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalBuyRequest.TerminalID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='AccountID', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalBuyRequest.AccountID', index=1,
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
  serialized_start=421,
  serialized_end=480,
)


_TERMINALBUYRESPONSE = _descriptor.Descriptor(
  name='TerminalBuyResponse',
  full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalBuyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Error', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalBuyResponse.Error', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=482,
  serialized_end=518,
)


_TERMINALSCANREQUEST = _descriptor.Descriptor(
  name='TerminalScanRequest',
  full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalScanRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TerminalID', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalScanRequest.TerminalID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ProductID', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalScanRequest.ProductID', index=1,
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
  serialized_start=520,
  serialized_end=580,
)


_TERMINALSCANRESPONSE = _descriptor.Descriptor(
  name='TerminalScanResponse',
  full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalScanResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Error', full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalScanResponse.Error', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=582,
  serialized_end=619,
)


_ABORTREQUEST = _descriptor.Descriptor(
  name='AbortRequest',
  full_name='i6getraenkeabrechnungssystem3000.rpc.AbortRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TerminalID', full_name='i6getraenkeabrechnungssystem3000.rpc.AbortRequest.TerminalID', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=621,
  serialized_end=655,
)


_ABORTRESPONSE = _descriptor.Descriptor(
  name='AbortResponse',
  full_name='i6getraenkeabrechnungssystem3000.rpc.AbortResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Error', full_name='i6getraenkeabrechnungssystem3000.rpc.AbortResponse.Error', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=657,
  serialized_end=687,
)

_TERMINALSTATERESPONSE_ACCOUNT.containing_type = _TERMINALSTATERESPONSE
_TERMINALSTATERESPONSE_ORDER.containing_type = _TERMINALSTATERESPONSE
_TERMINALSTATERESPONSE.fields_by_name['Accounts'].message_type = _TERMINALSTATERESPONSE_ACCOUNT
_TERMINALSTATERESPONSE.fields_by_name['OrderList'].message_type = _TERMINALSTATERESPONSE_ORDER
DESCRIPTOR.message_types_by_name['TerminalStateRequest'] = _TERMINALSTATEREQUEST
DESCRIPTOR.message_types_by_name['TerminalStateResponse'] = _TERMINALSTATERESPONSE
DESCRIPTOR.message_types_by_name['TerminalBuyRequest'] = _TERMINALBUYREQUEST
DESCRIPTOR.message_types_by_name['TerminalBuyResponse'] = _TERMINALBUYRESPONSE
DESCRIPTOR.message_types_by_name['TerminalScanRequest'] = _TERMINALSCANREQUEST
DESCRIPTOR.message_types_by_name['TerminalScanResponse'] = _TERMINALSCANRESPONSE
DESCRIPTOR.message_types_by_name['AbortRequest'] = _ABORTREQUEST
DESCRIPTOR.message_types_by_name['AbortResponse'] = _ABORTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TerminalStateRequest = _reflection.GeneratedProtocolMessageType('TerminalStateRequest', (_message.Message,), dict(
  DESCRIPTOR = _TERMINALSTATEREQUEST,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:i6getraenkeabrechnungssystem3000.rpc.TerminalStateRequest)
  ))
_sym_db.RegisterMessage(TerminalStateRequest)

TerminalStateResponse = _reflection.GeneratedProtocolMessageType('TerminalStateResponse', (_message.Message,), dict(

  Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), dict(
    DESCRIPTOR = _TERMINALSTATERESPONSE_ACCOUNT,
    __module__ = 'main_pb2'
    # @@protoc_insertion_point(class_scope:i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Account)
    ))
  ,

  Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), dict(
    DESCRIPTOR = _TERMINALSTATERESPONSE_ORDER,
    __module__ = 'main_pb2'
    # @@protoc_insertion_point(class_scope:i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse.Order)
    ))
  ,
  DESCRIPTOR = _TERMINALSTATERESPONSE,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:i6getraenkeabrechnungssystem3000.rpc.TerminalStateResponse)
  ))
_sym_db.RegisterMessage(TerminalStateResponse)
_sym_db.RegisterMessage(TerminalStateResponse.Account)
_sym_db.RegisterMessage(TerminalStateResponse.Order)

TerminalBuyRequest = _reflection.GeneratedProtocolMessageType('TerminalBuyRequest', (_message.Message,), dict(
  DESCRIPTOR = _TERMINALBUYREQUEST,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:i6getraenkeabrechnungssystem3000.rpc.TerminalBuyRequest)
  ))
_sym_db.RegisterMessage(TerminalBuyRequest)

TerminalBuyResponse = _reflection.GeneratedProtocolMessageType('TerminalBuyResponse', (_message.Message,), dict(
  DESCRIPTOR = _TERMINALBUYRESPONSE,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:i6getraenkeabrechnungssystem3000.rpc.TerminalBuyResponse)
  ))
_sym_db.RegisterMessage(TerminalBuyResponse)

TerminalScanRequest = _reflection.GeneratedProtocolMessageType('TerminalScanRequest', (_message.Message,), dict(
  DESCRIPTOR = _TERMINALSCANREQUEST,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:i6getraenkeabrechnungssystem3000.rpc.TerminalScanRequest)
  ))
_sym_db.RegisterMessage(TerminalScanRequest)

TerminalScanResponse = _reflection.GeneratedProtocolMessageType('TerminalScanResponse', (_message.Message,), dict(
  DESCRIPTOR = _TERMINALSCANRESPONSE,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:i6getraenkeabrechnungssystem3000.rpc.TerminalScanResponse)
  ))
_sym_db.RegisterMessage(TerminalScanResponse)

AbortRequest = _reflection.GeneratedProtocolMessageType('AbortRequest', (_message.Message,), dict(
  DESCRIPTOR = _ABORTREQUEST,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:i6getraenkeabrechnungssystem3000.rpc.AbortRequest)
  ))
_sym_db.RegisterMessage(AbortRequest)

AbortResponse = _reflection.GeneratedProtocolMessageType('AbortResponse', (_message.Message,), dict(
  DESCRIPTOR = _ABORTRESPONSE,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:i6getraenkeabrechnungssystem3000.rpc.AbortResponse)
  ))
_sym_db.RegisterMessage(AbortResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\003rpc'))

_TERMINALBACKEND = _descriptor.ServiceDescriptor(
  name='TerminalBackend',
  full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalBackend',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=690,
  serialized_end=1214,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetState',
    full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalBackend.GetState',
    index=0,
    containing_service=None,
    input_type=_TERMINALSTATEREQUEST,
    output_type=_TERMINALSTATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Buy',
    full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalBackend.Buy',
    index=1,
    containing_service=None,
    input_type=_TERMINALBUYREQUEST,
    output_type=_TERMINALBUYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Scan',
    full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalBackend.Scan',
    index=2,
    containing_service=None,
    input_type=_TERMINALSCANREQUEST,
    output_type=_TERMINALSCANRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Abort',
    full_name='i6getraenkeabrechnungssystem3000.rpc.TerminalBackend.Abort',
    index=3,
    containing_service=None,
    input_type=_ABORTREQUEST,
    output_type=_ABORTRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TERMINALBACKEND)

DESCRIPTOR.services_by_name['TerminalBackend'] = _TERMINALBACKEND

# @@protoc_insertion_point(module_scope)