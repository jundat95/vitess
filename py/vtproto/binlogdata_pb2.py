# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: binlogdata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import query_pb2 as query__pb2
import topodata_pb2 as topodata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='binlogdata.proto',
  package='binlogdata',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x62inlogdata.proto\x12\nbinlogdata\x1a\x0bquery.proto\x1a\x0etopodata.proto\"7\n\x07\x43harset\x12\x0e\n\x06\x63lient\x18\x01 \x01(\x05\x12\x0c\n\x04\x63onn\x18\x02 \x01(\x05\x12\x0e\n\x06server\x18\x03 \x01(\x05\"\xf3\x02\n\x11\x42inlogTransaction\x12;\n\nstatements\x18\x01 \x03(\x0b\x32\'.binlogdata.BinlogTransaction.Statement\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x16\n\x0etransaction_id\x18\x03 \x01(\t\x1a\xf5\x01\n\tStatement\x12\x42\n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32\x30.binlogdata.BinlogTransaction.Statement.Category\x12$\n\x07\x63harset\x18\x03 \x01(\x0b\x32\x13.binlogdata.Charset\x12\x0b\n\x03sql\x18\x02 \x01(\x0c\"q\n\x08\x43\x61tegory\x12\x13\n\x0f\x42L_UNRECOGNIZED\x10\x00\x12\x0c\n\x08\x42L_BEGIN\x10\x01\x12\r\n\tBL_COMMIT\x10\x02\x12\x0f\n\x0b\x42L_ROLLBACK\x10\x03\x12\n\n\x06\x42L_DML\x10\x04\x12\n\n\x06\x42L_DDL\x10\x05\x12\n\n\x06\x42L_SET\x10\x06\"\x9b\x02\n\x0bStreamEvent\x12\x32\n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32 .binlogdata.StreamEvent.Category\x12\x12\n\ntable_name\x18\x02 \x01(\t\x12(\n\x12primary_key_fields\x18\x03 \x03(\x0b\x32\x0c.query.Field\x12&\n\x12primary_key_values\x18\x04 \x03(\x0b\x32\n.query.Row\x12\x0b\n\x03sql\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\x12\x16\n\x0etransaction_id\x18\x07 \x01(\t\":\n\x08\x43\x61tegory\x12\n\n\x06SE_ERR\x10\x00\x12\n\n\x06SE_DML\x10\x01\x12\n\n\x06SE_DDL\x10\x02\x12\n\n\x06SE_POS\x10\x03\"\'\n\x13StreamUpdateRequest\x12\x10\n\x08position\x18\x01 \x01(\t\"E\n\x14StreamUpdateResponse\x12-\n\x0cstream_event\x18\x01 \x01(\x0b\x32\x17.binlogdata.StreamEvent\"\xaa\x01\n\x15StreamKeyRangeRequest\x12\x10\n\x08position\x18\x01 \x01(\t\x12\x32\n\x10keyspace_id_type\x18\x02 \x01(\x0e\x32\x18.topodata.KeyspaceIdType\x12%\n\tkey_range\x18\x03 \x01(\x0b\x32\x12.topodata.KeyRange\x12$\n\x07\x63harset\x18\x04 \x01(\x0b\x32\x13.binlogdata.Charset\"S\n\x16StreamKeyRangeResponse\x12\x39\n\x12\x62inlog_transaction\x18\x01 \x01(\x0b\x32\x1d.binlogdata.BinlogTransaction\"]\n\x13StreamTablesRequest\x12\x10\n\x08position\x18\x01 \x01(\t\x12\x0e\n\x06tables\x18\x02 \x03(\t\x12$\n\x07\x63harset\x18\x03 \x01(\x0b\x32\x13.binlogdata.Charset\"Q\n\x14StreamTablesResponse\x12\x39\n\x12\x62inlog_transaction\x18\x01 \x01(\x0b\x32\x1d.binlogdata.BinlogTransactionb\x06proto3')
  ,
  dependencies=[query__pb2.DESCRIPTOR,topodata__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BINLOGTRANSACTION_STATEMENT_CATEGORY = _descriptor.EnumDescriptor(
  name='Category',
  full_name='binlogdata.BinlogTransaction.Statement.Category',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BL_UNRECOGNIZED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BL_BEGIN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BL_COMMIT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BL_ROLLBACK', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BL_DML', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BL_DDL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BL_SET', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=377,
  serialized_end=490,
)
_sym_db.RegisterEnumDescriptor(_BINLOGTRANSACTION_STATEMENT_CATEGORY)

_STREAMEVENT_CATEGORY = _descriptor.EnumDescriptor(
  name='Category',
  full_name='binlogdata.StreamEvent.Category',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SE_ERR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SE_DML', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SE_DDL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SE_POS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=718,
  serialized_end=776,
)
_sym_db.RegisterEnumDescriptor(_STREAMEVENT_CATEGORY)


_CHARSET = _descriptor.Descriptor(
  name='Charset',
  full_name='binlogdata.Charset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client', full_name='binlogdata.Charset.client', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conn', full_name='binlogdata.Charset.conn', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server', full_name='binlogdata.Charset.server', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=116,
)


_BINLOGTRANSACTION_STATEMENT = _descriptor.Descriptor(
  name='Statement',
  full_name='binlogdata.BinlogTransaction.Statement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='binlogdata.BinlogTransaction.Statement.category', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='charset', full_name='binlogdata.BinlogTransaction.Statement.charset', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sql', full_name='binlogdata.BinlogTransaction.Statement.sql', index=2,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BINLOGTRANSACTION_STATEMENT_CATEGORY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=490,
)

_BINLOGTRANSACTION = _descriptor.Descriptor(
  name='BinlogTransaction',
  full_name='binlogdata.BinlogTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statements', full_name='binlogdata.BinlogTransaction.statements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='binlogdata.BinlogTransaction.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='binlogdata.BinlogTransaction.transaction_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BINLOGTRANSACTION_STATEMENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=490,
)


_STREAMEVENT = _descriptor.Descriptor(
  name='StreamEvent',
  full_name='binlogdata.StreamEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='binlogdata.StreamEvent.category', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='binlogdata.StreamEvent.table_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='primary_key_fields', full_name='binlogdata.StreamEvent.primary_key_fields', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='primary_key_values', full_name='binlogdata.StreamEvent.primary_key_values', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sql', full_name='binlogdata.StreamEvent.sql', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='binlogdata.StreamEvent.timestamp', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='binlogdata.StreamEvent.transaction_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STREAMEVENT_CATEGORY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=776,
)


_STREAMUPDATEREQUEST = _descriptor.Descriptor(
  name='StreamUpdateRequest',
  full_name='binlogdata.StreamUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='binlogdata.StreamUpdateRequest.position', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=817,
)


_STREAMUPDATERESPONSE = _descriptor.Descriptor(
  name='StreamUpdateResponse',
  full_name='binlogdata.StreamUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_event', full_name='binlogdata.StreamUpdateResponse.stream_event', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=819,
  serialized_end=888,
)


_STREAMKEYRANGEREQUEST = _descriptor.Descriptor(
  name='StreamKeyRangeRequest',
  full_name='binlogdata.StreamKeyRangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='binlogdata.StreamKeyRangeRequest.position', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyspace_id_type', full_name='binlogdata.StreamKeyRangeRequest.keyspace_id_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_range', full_name='binlogdata.StreamKeyRangeRequest.key_range', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='charset', full_name='binlogdata.StreamKeyRangeRequest.charset', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=891,
  serialized_end=1061,
)


_STREAMKEYRANGERESPONSE = _descriptor.Descriptor(
  name='StreamKeyRangeResponse',
  full_name='binlogdata.StreamKeyRangeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binlog_transaction', full_name='binlogdata.StreamKeyRangeResponse.binlog_transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1063,
  serialized_end=1146,
)


_STREAMTABLESREQUEST = _descriptor.Descriptor(
  name='StreamTablesRequest',
  full_name='binlogdata.StreamTablesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='binlogdata.StreamTablesRequest.position', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tables', full_name='binlogdata.StreamTablesRequest.tables', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='charset', full_name='binlogdata.StreamTablesRequest.charset', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1148,
  serialized_end=1241,
)


_STREAMTABLESRESPONSE = _descriptor.Descriptor(
  name='StreamTablesResponse',
  full_name='binlogdata.StreamTablesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binlog_transaction', full_name='binlogdata.StreamTablesResponse.binlog_transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1243,
  serialized_end=1324,
)

_BINLOGTRANSACTION_STATEMENT.fields_by_name['category'].enum_type = _BINLOGTRANSACTION_STATEMENT_CATEGORY
_BINLOGTRANSACTION_STATEMENT.fields_by_name['charset'].message_type = _CHARSET
_BINLOGTRANSACTION_STATEMENT.containing_type = _BINLOGTRANSACTION
_BINLOGTRANSACTION_STATEMENT_CATEGORY.containing_type = _BINLOGTRANSACTION_STATEMENT
_BINLOGTRANSACTION.fields_by_name['statements'].message_type = _BINLOGTRANSACTION_STATEMENT
_STREAMEVENT.fields_by_name['category'].enum_type = _STREAMEVENT_CATEGORY
_STREAMEVENT.fields_by_name['primary_key_fields'].message_type = query__pb2._FIELD
_STREAMEVENT.fields_by_name['primary_key_values'].message_type = query__pb2._ROW
_STREAMEVENT_CATEGORY.containing_type = _STREAMEVENT
_STREAMUPDATERESPONSE.fields_by_name['stream_event'].message_type = _STREAMEVENT
_STREAMKEYRANGEREQUEST.fields_by_name['keyspace_id_type'].enum_type = topodata__pb2._KEYSPACEIDTYPE
_STREAMKEYRANGEREQUEST.fields_by_name['key_range'].message_type = topodata__pb2._KEYRANGE
_STREAMKEYRANGEREQUEST.fields_by_name['charset'].message_type = _CHARSET
_STREAMKEYRANGERESPONSE.fields_by_name['binlog_transaction'].message_type = _BINLOGTRANSACTION
_STREAMTABLESREQUEST.fields_by_name['charset'].message_type = _CHARSET
_STREAMTABLESRESPONSE.fields_by_name['binlog_transaction'].message_type = _BINLOGTRANSACTION
DESCRIPTOR.message_types_by_name['Charset'] = _CHARSET
DESCRIPTOR.message_types_by_name['BinlogTransaction'] = _BINLOGTRANSACTION
DESCRIPTOR.message_types_by_name['StreamEvent'] = _STREAMEVENT
DESCRIPTOR.message_types_by_name['StreamUpdateRequest'] = _STREAMUPDATEREQUEST
DESCRIPTOR.message_types_by_name['StreamUpdateResponse'] = _STREAMUPDATERESPONSE
DESCRIPTOR.message_types_by_name['StreamKeyRangeRequest'] = _STREAMKEYRANGEREQUEST
DESCRIPTOR.message_types_by_name['StreamKeyRangeResponse'] = _STREAMKEYRANGERESPONSE
DESCRIPTOR.message_types_by_name['StreamTablesRequest'] = _STREAMTABLESREQUEST
DESCRIPTOR.message_types_by_name['StreamTablesResponse'] = _STREAMTABLESRESPONSE

Charset = _reflection.GeneratedProtocolMessageType('Charset', (_message.Message,), dict(
  DESCRIPTOR = _CHARSET,
  __module__ = 'binlogdata_pb2'
  # @@protoc_insertion_point(class_scope:binlogdata.Charset)
  ))
_sym_db.RegisterMessage(Charset)

BinlogTransaction = _reflection.GeneratedProtocolMessageType('BinlogTransaction', (_message.Message,), dict(

  Statement = _reflection.GeneratedProtocolMessageType('Statement', (_message.Message,), dict(
    DESCRIPTOR = _BINLOGTRANSACTION_STATEMENT,
    __module__ = 'binlogdata_pb2'
    # @@protoc_insertion_point(class_scope:binlogdata.BinlogTransaction.Statement)
    ))
  ,
  DESCRIPTOR = _BINLOGTRANSACTION,
  __module__ = 'binlogdata_pb2'
  # @@protoc_insertion_point(class_scope:binlogdata.BinlogTransaction)
  ))
_sym_db.RegisterMessage(BinlogTransaction)
_sym_db.RegisterMessage(BinlogTransaction.Statement)

StreamEvent = _reflection.GeneratedProtocolMessageType('StreamEvent', (_message.Message,), dict(
  DESCRIPTOR = _STREAMEVENT,
  __module__ = 'binlogdata_pb2'
  # @@protoc_insertion_point(class_scope:binlogdata.StreamEvent)
  ))
_sym_db.RegisterMessage(StreamEvent)

StreamUpdateRequest = _reflection.GeneratedProtocolMessageType('StreamUpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMUPDATEREQUEST,
  __module__ = 'binlogdata_pb2'
  # @@protoc_insertion_point(class_scope:binlogdata.StreamUpdateRequest)
  ))
_sym_db.RegisterMessage(StreamUpdateRequest)

StreamUpdateResponse = _reflection.GeneratedProtocolMessageType('StreamUpdateResponse', (_message.Message,), dict(
  DESCRIPTOR = _STREAMUPDATERESPONSE,
  __module__ = 'binlogdata_pb2'
  # @@protoc_insertion_point(class_scope:binlogdata.StreamUpdateResponse)
  ))
_sym_db.RegisterMessage(StreamUpdateResponse)

StreamKeyRangeRequest = _reflection.GeneratedProtocolMessageType('StreamKeyRangeRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMKEYRANGEREQUEST,
  __module__ = 'binlogdata_pb2'
  # @@protoc_insertion_point(class_scope:binlogdata.StreamKeyRangeRequest)
  ))
_sym_db.RegisterMessage(StreamKeyRangeRequest)

StreamKeyRangeResponse = _reflection.GeneratedProtocolMessageType('StreamKeyRangeResponse', (_message.Message,), dict(
  DESCRIPTOR = _STREAMKEYRANGERESPONSE,
  __module__ = 'binlogdata_pb2'
  # @@protoc_insertion_point(class_scope:binlogdata.StreamKeyRangeResponse)
  ))
_sym_db.RegisterMessage(StreamKeyRangeResponse)

StreamTablesRequest = _reflection.GeneratedProtocolMessageType('StreamTablesRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMTABLESREQUEST,
  __module__ = 'binlogdata_pb2'
  # @@protoc_insertion_point(class_scope:binlogdata.StreamTablesRequest)
  ))
_sym_db.RegisterMessage(StreamTablesRequest)

StreamTablesResponse = _reflection.GeneratedProtocolMessageType('StreamTablesResponse', (_message.Message,), dict(
  DESCRIPTOR = _STREAMTABLESRESPONSE,
  __module__ = 'binlogdata_pb2'
  # @@protoc_insertion_point(class_scope:binlogdata.StreamTablesResponse)
  ))
_sym_db.RegisterMessage(StreamTablesResponse)


import abc
from grpc.early_adopter import implementations
from grpc.framework.alpha import utilities
# @@protoc_insertion_point(module_scope)
