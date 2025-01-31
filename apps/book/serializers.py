import uuid
from typing import Literal
from typing import Optional

from pydantic import BaseModel, validator, Field

from apps.book.models import Book


class BookBaseSerializer(BaseModel):
    id: Optional[int] = None
    title: str
    units: int
    status: str
    isbn: str
    price: float
    description: str
    genre_id: int


class BookCreateSerializer(BaseModel):
    title: str = Field(min_length=1, max_length=255, description="Book title")
    units: int = Field(description="Book units", default=uuid.uuid4().int)
    status: Literal["Available", "Reserved"] = Field(description="Book status", default="Available")
    isbn: str = Field(description="Book isbn", default=str(uuid.uuid4().int)[-1 * 13:])
    price: float = Field(ge=0, description="Book price")
    description: str = Field(description="Book description")
    genre_id: int = Field(description="Book genre id")

    @validator("isbn")
    def validate_isbn(cls, value):
        if Book.objects.get(isbn=value):
            return str(uuid.uuid4().int)[-1 * 13:]
        return value

    @validator("units")
    def validate_units(cls, value):
        if Book.objects.get(units=value):
            return uuid.uuid4().int
        return value


class BookUpdateSerializer(BaseModel):
    title: str = Field(min_length=1, max_length=255, description="Book title", default=None)
    status: Literal["Available", "Reserved"] = Field(description="Book status", default=None)
    price: float = Field(ge=0, description="Book price", default=None)
    description: str = Field(description="Book description", default=None)
    genre_id: int = Field(description="Book genre id", default=None)
