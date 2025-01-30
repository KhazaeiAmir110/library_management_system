from typing import Optional

from pydantic import BaseModel


class BookBaseSerializer(BaseModel):
    id: Optional[int] = None
    title: str
    units: int
    status: str
    isbn: str
    price: float
    description: str
    genre_id: int


class BookUpdateSerializer(BookBaseSerializer):
    title: Optional[str] = None
    units: Optional[int] = None
    status: Optional[str] = None
    isbn: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    genre_id: Optional[int] = None