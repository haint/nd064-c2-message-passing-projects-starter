from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LocationMessage(_message.Message):
    __slots__ = ["latitude", "longitude", "person_id", "timestamp"]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    latitude: str
    longitude: str
    person_id: int
    timestamp: int
    def __init__(self, person_id: _Optional[int] = ..., latitude: _Optional[str] = ..., longitude: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...
