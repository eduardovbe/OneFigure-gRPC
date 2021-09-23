# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/message.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13proto/message.proto\x12\x05proto\"\xd9\x01\n\rMessageClient\x12\x13\n\x06idUser\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x15\n\x08idFigure\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x14\n\x07idOffer\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x15\n\x08idTaking\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x11\n\x04name\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x15\n\x08password\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\t\n\x07_idUserB\x0b\n\t_idFigureB\n\n\x08_idOfferB\x0b\n\t_idTakingB\x07\n\x05_nameB\x0b\n\t_password\"\x8a\x01\n\x06\x46igure\x12\x10\n\x08idFigure\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06rarity\x18\x03 \x01(\t\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\x15\n\x08quantity\x18\x05 \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06idUser\x18\x06 \x01(\x05H\x01\x88\x01\x01\x42\x0b\n\t_quantityB\t\n\x07_idUser\"Y\n\x04User\x12\x0e\n\x06idUser\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x02\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x10\n\x08showcard\x18\x05 \x01(\x08\"k\n\rLoginResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\x12\x19\n\x04user\x18\x02 \x01(\x0b\x32\x0b.proto.User\x12\"\n\x06\x66igure\x18\x03 \x01(\x0b\x32\r.proto.FigureH\x00\x88\x01\x01\x42\t\n\x07_figure\"\x94\x01\n\rAlbumResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\x12\x10\n\x08\x63omplete\x18\x02 \x01(\x08\x12\x0e\n\x06idUser\x18\x03 \x01(\x05\x12#\n\x07special\x18\x04 \x01(\x0b\x32\r.proto.FigureH\x00\x88\x01\x01\x12\x1e\n\x07\x66igures\x18\x05 \x03(\x0b\x32\r.proto.FigureB\n\n\x08_special\"\x1c\n\x08Response\x12\x10\n\x08response\x18\x01 \x01(\x08\x32\xaa\x01\n\x07Message\x12\x35\n\x05Login\x12\x14.proto.MessageClient\x1a\x14.proto.LoginResponse\"\x00\x12\x31\n\x06\x43reate\x12\x14.proto.MessageClient\x1a\x0f.proto.Response\"\x00\x12\x35\n\x05\x41lbum\x12\x14.proto.MessageClient\x1a\x14.proto.AlbumResponse\"\x00\x62\x06proto3'
)




_MESSAGECLIENT = _descriptor.Descriptor(
  name='MessageClient',
  full_name='proto.MessageClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='idUser', full_name='proto.MessageClient.idUser', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idFigure', full_name='proto.MessageClient.idFigure', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idOffer', full_name='proto.MessageClient.idOffer', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idTaking', full_name='proto.MessageClient.idTaking', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.MessageClient.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='proto.MessageClient.password', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='_idUser', full_name='proto.MessageClient._idUser',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_idFigure', full_name='proto.MessageClient._idFigure',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_idOffer', full_name='proto.MessageClient._idOffer',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_idTaking', full_name='proto.MessageClient._idTaking',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_name', full_name='proto.MessageClient._name',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_password', full_name='proto.MessageClient._password',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=31,
  serialized_end=248,
)


_FIGURE = _descriptor.Descriptor(
  name='Figure',
  full_name='proto.Figure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='idFigure', full_name='proto.Figure.idFigure', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.Figure.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rarity', full_name='proto.Figure.rarity', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='proto.Figure.path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='proto.Figure.quantity', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idUser', full_name='proto.Figure.idUser', index=5,
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
      name='_quantity', full_name='proto.Figure._quantity',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_idUser', full_name='proto.Figure._idUser',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=251,
  serialized_end=389,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='proto.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='idUser', full_name='proto.User.idUser', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='balance', full_name='proto.User.balance', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='proto.User.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='showcard', full_name='proto.User.showcard', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=391,
  serialized_end=480,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='proto.LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='proto.LoginResponse.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='proto.LoginResponse.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='figure', full_name='proto.LoginResponse.figure', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='_figure', full_name='proto.LoginResponse._figure',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=482,
  serialized_end=589,
)


_ALBUMRESPONSE = _descriptor.Descriptor(
  name='AlbumResponse',
  full_name='proto.AlbumResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='proto.AlbumResponse.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='complete', full_name='proto.AlbumResponse.complete', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idUser', full_name='proto.AlbumResponse.idUser', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='special', full_name='proto.AlbumResponse.special', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='figures', full_name='proto.AlbumResponse.figures', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
      name='_special', full_name='proto.AlbumResponse._special',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=592,
  serialized_end=740,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='proto.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='proto.Response.response', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=742,
  serialized_end=770,
)

_MESSAGECLIENT.oneofs_by_name['_idUser'].fields.append(
  _MESSAGECLIENT.fields_by_name['idUser'])
_MESSAGECLIENT.fields_by_name['idUser'].containing_oneof = _MESSAGECLIENT.oneofs_by_name['_idUser']
_MESSAGECLIENT.oneofs_by_name['_idFigure'].fields.append(
  _MESSAGECLIENT.fields_by_name['idFigure'])
_MESSAGECLIENT.fields_by_name['idFigure'].containing_oneof = _MESSAGECLIENT.oneofs_by_name['_idFigure']
_MESSAGECLIENT.oneofs_by_name['_idOffer'].fields.append(
  _MESSAGECLIENT.fields_by_name['idOffer'])
_MESSAGECLIENT.fields_by_name['idOffer'].containing_oneof = _MESSAGECLIENT.oneofs_by_name['_idOffer']
_MESSAGECLIENT.oneofs_by_name['_idTaking'].fields.append(
  _MESSAGECLIENT.fields_by_name['idTaking'])
_MESSAGECLIENT.fields_by_name['idTaking'].containing_oneof = _MESSAGECLIENT.oneofs_by_name['_idTaking']
_MESSAGECLIENT.oneofs_by_name['_name'].fields.append(
  _MESSAGECLIENT.fields_by_name['name'])
_MESSAGECLIENT.fields_by_name['name'].containing_oneof = _MESSAGECLIENT.oneofs_by_name['_name']
_MESSAGECLIENT.oneofs_by_name['_password'].fields.append(
  _MESSAGECLIENT.fields_by_name['password'])
_MESSAGECLIENT.fields_by_name['password'].containing_oneof = _MESSAGECLIENT.oneofs_by_name['_password']
_FIGURE.oneofs_by_name['_quantity'].fields.append(
  _FIGURE.fields_by_name['quantity'])
_FIGURE.fields_by_name['quantity'].containing_oneof = _FIGURE.oneofs_by_name['_quantity']
_FIGURE.oneofs_by_name['_idUser'].fields.append(
  _FIGURE.fields_by_name['idUser'])
_FIGURE.fields_by_name['idUser'].containing_oneof = _FIGURE.oneofs_by_name['_idUser']
_LOGINRESPONSE.fields_by_name['user'].message_type = _USER
_LOGINRESPONSE.fields_by_name['figure'].message_type = _FIGURE
_LOGINRESPONSE.oneofs_by_name['_figure'].fields.append(
  _LOGINRESPONSE.fields_by_name['figure'])
_LOGINRESPONSE.fields_by_name['figure'].containing_oneof = _LOGINRESPONSE.oneofs_by_name['_figure']
_ALBUMRESPONSE.fields_by_name['special'].message_type = _FIGURE
_ALBUMRESPONSE.fields_by_name['figures'].message_type = _FIGURE
_ALBUMRESPONSE.oneofs_by_name['_special'].fields.append(
  _ALBUMRESPONSE.fields_by_name['special'])
_ALBUMRESPONSE.fields_by_name['special'].containing_oneof = _ALBUMRESPONSE.oneofs_by_name['_special']
DESCRIPTOR.message_types_by_name['MessageClient'] = _MESSAGECLIENT
DESCRIPTOR.message_types_by_name['Figure'] = _FIGURE
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
DESCRIPTOR.message_types_by_name['AlbumResponse'] = _ALBUMRESPONSE
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageClient = _reflection.GeneratedProtocolMessageType('MessageClient', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGECLIENT,
  '__module__' : 'proto.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.MessageClient)
  })
_sym_db.RegisterMessage(MessageClient)

Figure = _reflection.GeneratedProtocolMessageType('Figure', (_message.Message,), {
  'DESCRIPTOR' : _FIGURE,
  '__module__' : 'proto.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.Figure)
  })
_sym_db.RegisterMessage(Figure)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'proto.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.User)
  })
_sym_db.RegisterMessage(User)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'proto.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)

AlbumResponse = _reflection.GeneratedProtocolMessageType('AlbumResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALBUMRESPONSE,
  '__module__' : 'proto.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.AlbumResponse)
  })
_sym_db.RegisterMessage(AlbumResponse)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'proto.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.Response)
  })
_sym_db.RegisterMessage(Response)



_MESSAGE = _descriptor.ServiceDescriptor(
  name='Message',
  full_name='proto.Message',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=773,
  serialized_end=943,
  methods=[
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='proto.Message.Login',
    index=0,
    containing_service=None,
    input_type=_MESSAGECLIENT,
    output_type=_LOGINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='proto.Message.Create',
    index=1,
    containing_service=None,
    input_type=_MESSAGECLIENT,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Album',
    full_name='proto.Message.Album',
    index=2,
    containing_service=None,
    input_type=_MESSAGECLIENT,
    output_type=_ALBUMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSAGE)

DESCRIPTOR.services_by_name['Message'] = _MESSAGE

# @@protoc_insertion_point(module_scope)
