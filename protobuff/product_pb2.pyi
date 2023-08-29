from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Pagination(_message.Message):
    __slots__ = ["total", "per_page", "current_page", "last_page"]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    total: int
    per_page: int
    current_page: int
    last_page: int
    def __init__(self, total: _Optional[int] = ..., per_page: _Optional[int] = ..., current_page: _Optional[int] = ..., last_page: _Optional[int] = ...) -> None: ...

class Products(_message.Message):
    __slots__ = ["pagination", "data"]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    pagination: Pagination
    data: _containers.RepeatedCompositeFieldContainer[Product]
    def __init__(self, pagination: _Optional[_Union[Pagination, _Mapping]] = ..., data: _Optional[_Iterable[_Union[Product, _Mapping]]] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ["id", "name", "price", "stock", "category"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    price: float
    stock: int
    category: Category
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., price: _Optional[float] = ..., stock: _Optional[int] = ..., category: _Optional[_Union[Category, _Mapping]] = ...) -> None: ...

class Category(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class Id(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class Page(_message.Message):
    __slots__ = ["page", "per_page"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    page: int
    per_page: int
    def __init__(self, page: _Optional[int] = ..., per_page: _Optional[int] = ...) -> None: ...
