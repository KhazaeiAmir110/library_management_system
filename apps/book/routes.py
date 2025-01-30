from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from apps.book.models import Book, City, Genre, Author, BookManager
from typing import List

router = APIRouter(
    prefix="/book",
    tags=["Company"]
)


class BookModel(BaseModel):
    name: str
    type: str
    status: str
    price: float
    description: str
    author_id: int
    city_id: int
    genre_id: int


class BookResponse(BookModel):
    id: int


@router.post("/books/", response_model=BookResponse)
async def create_book(book: BookModel):
    book_id = await BookModel.objects.create(book)
    return {**book.dict(), "id": book_id}


@router.get("/books/", response_model=List[BookResponse])
async def get_books():
    books = await Book.objects.all()
    return books


@router.get("/books/{book_id}", response_model=BookResponse)
async def get_book(book_id: int):
    book = await Book.objects.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
