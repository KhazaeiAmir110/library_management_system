from typing import List

from fastapi import APIRouter, HTTPException, responses
from starlette import status

from apps.book.models import Book
from apps.book.serializers import BookBaseSerializer, BookUpdateSerializer, BookCreateSerializer

router = APIRouter(prefix="/book", tags=["Book"])


@router.post("/")
async def create_book(book: BookCreateSerializer):
    try:
        Book.objects.create(
            title=book.title,
            units=book.units,
            status=book.status,
            isbn=book.isbn,
            price=book.price,
            description=book.description,
            genre_id=book.genre_id
        )
        return responses.Response(status_code=status.HTTP_201_CREATED)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


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
async def get_book(book_id: int):
    try:
        book = Book.objects.get(id=book_id)
        return BookBaseSerializer(**dict(zip(BookBaseSerializer.model_fields.keys(), book)))

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{book_id}")
async def update_book(book_id: int, book: BookUpdateSerializer):
    try:
        update_data = {key: value for key, value in book.dict().items() if value is not None}
        Book.objects.update(id=book_id, **update_data)

        return BookUpdateSerializer(**dict(zip(BookUpdateSerializer.model_fields.keys(), Book.objects.get(id=book_id))))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{book_id}")
async def delete_book(book_id: int):
    try:
        Book.objects.delete(id=book_id)
        return responses.Response(status_code=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
