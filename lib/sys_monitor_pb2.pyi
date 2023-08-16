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
    total: float
    used: float
    free: float
    def __init__(self, total: _Optional[float] = ..., used: _Optional[float] = ..., free: _Optional[float] = ...) -> None: ...

class CPUFreq(_message.Message):
    __slots__ = ["current"]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    current: float
    def __init__(self, current: _Optional[float] = ...) -> None: ...

class DISkinfo(_message.Message):
    __slots__ = ["total", "used", "free"]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    FREE_FIELD_NUMBER: _ClassVar[int]
    total: float
    used: float
    free: float
    def __init__(self, total: _Optional[float] = ..., used: _Optional[float] = ..., free: _Optional[float] = ...) -> None: ...
