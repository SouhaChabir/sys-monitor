from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RAMinfo(_message.Message):
    __slots__ = ["total", "used", "free"]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    FREE_FIELD_NUMBER: _ClassVar[int]
    total: int
    used: int
    free: int
    def __init__(self, total: _Optional[int] = ..., used: _Optional[int] = ..., free: _Optional[int] = ...) -> None: ...

class CPUFreq(_message.Message):
    __slots__ = ["current", "min", "max"]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    current: int
    min: int
    max: int
    def __init__(self, current: _Optional[int] = ..., min: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...

class DISkinfo(_message.Message):
    __slots__ = ["total", "used", "free"]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    FREE_FIELD_NUMBER: _ClassVar[int]
    total: int
    used: int
    free: int
    def __init__(self, total: _Optional[int] = ..., used: _Optional[int] = ..., free: _Optional[int] = ...) -> None: ...
