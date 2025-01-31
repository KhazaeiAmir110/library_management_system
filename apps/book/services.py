from fastapi import HTTPException, status, responses
from starlette.responses import Response

from apps.book.models import Book
from apps.book.serializers import BookCreateSerializer, BookUpdateSerializer, BookBaseSerializer


class BookService:
    @staticmethod
    def create_book(book_data: BookCreateSerializer) -> Response:
        try:
            Book.objects.create(
                title=book_data.title,
                units=book_data.units,
                status=book_data.status,
                isbn=book_data.isbn,
                price=book_data.price,
                description=book_data.description,
                genre_id=book_data.genre_id
            )
            return responses.Response(status_code=status.HTTP_201_CREATED)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def get_book(book_id: int) -> BookBaseSerializer:
        try:
            book = Book.objects.get(id=book_id)
            return BookBaseSerializer(**dict(zip(BookBaseSerializer.model_fields.keys(), book)))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def update_book(book_id: int, book: BookUpdateSerializer) -> BookBaseSerializer:
        try:
            if Book.objects.get(id=book_id) is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            update_data = {key: value for key, value in book.dict().items() if value is not None}
            Book.objects.update(id=book_id, **update_data)

            return BookService.get_book(book_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def delete_book(book_id: int) -> Response:
        try:
            Book.objects.delete(id=book_id)
            return responses.Response(status_code=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
