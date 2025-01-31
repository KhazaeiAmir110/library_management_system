from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from apps.book.models import Book
from apps.book.serializers import BookBaseSerializer, BookUpdateSerializer, BookCreateSerializer
from apps.book.services import BookService

router = APIRouter(prefix="/book", tags=["Book"])


@router.post("/")
async def create_book(book: BookCreateSerializer, status_code=201):
    return BookService.create_book(book)


@router.get("/", response_model=List[BookBaseSerializer])
async def list_books():
    try:
        books = Book.objects.all()
        book_list = [
            BookBaseSerializer(**{
                field_name: field_value
                for field_name, field_value in zip(BookBaseSerializer.__fields__.keys(), book)
            })
            for book in books
        ]
        return book_list
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{book_id}", response_model=BookBaseSerializer)
async def get_book(book_id: int, status_code=200):
    book = BookService.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return book


@router.patch("/{book_id}")
async def update_book(book_id: int, book: BookUpdateSerializer, status_code=200):
    return BookService.update_book(book_id, book)


@router.delete("/{book_id}")
async def delete_book(book_id: int, status_code=200):
    return BookService.delete_book(book_id)
