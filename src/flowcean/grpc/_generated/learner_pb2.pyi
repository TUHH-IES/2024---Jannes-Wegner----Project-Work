"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Status:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Status.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    STATUS_UNDEFINED: _Status.ValueType  # 0
    STATUS_RUNNING: _Status.ValueType  # 1
    STATUS_FINISHED: _Status.ValueType  # 2
    STATUS_FAILED: _Status.ValueType  # 3

class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...

STATUS_UNDEFINED: Status.ValueType  # 0
STATUS_RUNNING: Status.ValueType  # 1
STATUS_FINISHED: Status.ValueType  # 2
STATUS_FAILED: Status.ValueType  # 3
global___Status = Status

class _LogLevel:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _LogLevelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LogLevel.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    LOGLEVEL_UNDEFINED: _LogLevel.ValueType  # 0
    LOGLEVEL_DEBUG: _LogLevel.ValueType  # 1
    LOGLEVEL_INFO: _LogLevel.ValueType  # 2
    LOGLEVEL_WARNING: _LogLevel.ValueType  # 3
    LOGLEVEL_ERROR: _LogLevel.ValueType  # 4
    LOGLEVEL_FATAL: _LogLevel.ValueType  # 5

class LogLevel(_LogLevel, metaclass=_LogLevelEnumTypeWrapper): ...

LOGLEVEL_UNDEFINED: LogLevel.ValueType  # 0
LOGLEVEL_DEBUG: LogLevel.ValueType  # 1
LOGLEVEL_INFO: LogLevel.ValueType  # 2
LOGLEVEL_WARNING: LogLevel.ValueType  # 3
LOGLEVEL_ERROR: LogLevel.ValueType  # 4
LOGLEVEL_FATAL: LogLevel.ValueType  # 5
global___LogLevel = LogLevel

@typing.final
class DataPackage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INPUTS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    @property
    def inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TimeSeries]: ...
    @property
    def outputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TimeSeries]: ...
    def __init__(
        self,
        *,
        inputs: collections.abc.Iterable[global___TimeSeries] | None = ...,
        outputs: collections.abc.Iterable[global___TimeSeries] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["inputs", b"inputs", "outputs", b"outputs"]) -> None: ...

global___DataPackage = DataPackage

@typing.final
class Prediction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PREDICTIONS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    @property
    def predictions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TimeSeries]: ...
    @property
    def status(self) -> global___StatusMessage: ...
    def __init__(
        self,
        *,
        predictions: collections.abc.Iterable[global___TimeSeries] | None = ...,
        status: global___StatusMessage | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["predictions", b"predictions", "status", b"status"]) -> None: ...

global___Prediction = Prediction

@typing.final
class TimeSeries(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SAMPLES_FIELD_NUMBER: builtins.int
    @property
    def samples(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TimeSample]: ...
    def __init__(
        self,
        *,
        samples: collections.abc.Iterable[global___TimeSample] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["samples", b"samples"]) -> None: ...

global___TimeSeries = TimeSeries

@typing.final
class TimeSample(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    time: builtins.float
    @property
    def value(self) -> global___DataField: ...
    def __init__(
        self,
        *,
        time: builtins.float = ...,
        value: global___DataField | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["time", b"time", "value", b"value"]) -> None: ...

global___TimeSample = TimeSample

@typing.final
class DataField(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INT_FIELD_NUMBER: builtins.int
    DOUBLE_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    int: builtins.int
    double: builtins.float
    string: builtins.str
    def __init__(
        self,
        *,
        int: builtins.int = ...,
        double: builtins.float = ...,
        string: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["double", b"double", "field", b"field", "int", b"int", "string", b"string"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["double", b"double", "field", b"field", "int", b"int", "string", b"string"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["field", b"field"]) -> typing.Literal["int", "double", "string"] | None: ...

global___DataField = DataField

@typing.final
class StatusMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    MESSAGES_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    status: global___Status.ValueType
    progress: builtins.int
    @property
    def messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Message]: ...
    def __init__(
        self,
        *,
        status: global___Status.ValueType = ...,
        messages: collections.abc.Iterable[global___Message] | None = ...,
        progress: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_progress", b"_progress", "progress", b"progress"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_progress", b"_progress", "messages", b"messages", "progress", b"progress", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_progress", b"_progress"]) -> typing.Literal["progress"] | None: ...

global___StatusMessage = StatusMessage

@typing.final
class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOG_LEVEL_FIELD_NUMBER: builtins.int
    SENDER_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    log_level: global___LogLevel.ValueType
    sender: builtins.str
    message: builtins.str
    def __init__(
        self,
        *,
        log_level: global___LogLevel.ValueType = ...,
        sender: builtins.str = ...,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["log_level", b"log_level", "message", b"message", "sender", b"sender"]) -> None: ...

global___Message = Message

@typing.final
class Empty(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Empty = Empty
