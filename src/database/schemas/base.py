from typing import TypeVar

from pydantic import BaseModel

AddDTO: TypeVar = TypeVar("AddDTO", bound="BaseAddDTO")
DTO: TypeVar = TypeVar("DTO", bound="BaseDTO")
RelDTO: TypeVar = TypeVar("RelDTO", bound="BaseRelDTO")
SelectDTO: TypeVar = TypeVar("SelectDTO", bound="BaseSelectDTO")


class BaseAddDTO(BaseModel):
    pass


class BaseDTO(BaseModel):
    pass


class BaseRelDTO(BaseModel):
    pass


class BaseSelectDTO(BaseModel):
    pass
