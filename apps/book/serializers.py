import uuid
from typing import Literal, Optional

from pydantic import BaseModel, validator, Field

from apps.book.models import Book


class BookBaseSerializer(BaseModel):
    id: int
    title: str
    units: int
    status: str
    isbn: str
    price: float
    description: str
    genre_id: int


class BookCreateSerializer(BaseModel):
    title: str = Field(min_length=1, max_length=255, description="Book title")
    units: int = Field(description="Book units", default_factory=lambda: int(str(uuid.uuid4().int)[-1 * 5:]))
    status: Literal["Available", "Reserved"] = Field(description="Book status", default="Available")
    isbn: str = Field(description="Book isbn", default_factory=lambda: str(uuid.uuid4().int)[-1 * 13:])
    price: float = Field(ge=0, description="Book price")
    description: Optional[str] = Field(description="Book description", default=None)
    genre_id: int = Field(description="Book genre id")

    @validator("isbn")
    def validate_isbn(cls, value):
        if Book.objects.get(isbn=value) or value is None:
            return str(uuid.uuid4().int)[-1 * 13:]
        return value

    @validator("units")
    def validate_units(cls, value):
        if Book.objects.get(units=value) or value is None:
            return int(str(uuid.uuid4().int)[-1 * 5:])
        return value


class BookUpdateSerializer(BaseModel):
    title: str = Field(min_length=1, max_length=255, description="Book title", default=None)
    status: Literal["Available", "Reserved"] = Field(description="Book status", default=None)
    price: float = Field(ge=0, description="Book price", default=None)
    description: str = Field(description="Book description", default=None)
    genre_id: int = Field(description="Book genre id", default=None)
