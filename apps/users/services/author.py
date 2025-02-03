from fastapi import HTTPException, status, responses
from fastapi.responses import Response

from apps.users.models import Author
from apps.users.serializers import AuthorCreateSerializer, AuthorBaseSerializer, AuthorUpdateSerializer


class AuthorService:
    @staticmethod
    def create_author(user_data: AuthorCreateSerializer) -> Response:
        try:
            Author.objects.create(
                username=user_data.username,
                password=user_data.password,
                first_name=user_data.first_name,
                last_name=user_data.last_name,
                phone=user_data.phone,
                biography=user_data.biography,
                book_id=user_data.book_id,
                city_id=user_data.city_id,
                goodreads=user_data.goodreads,
                bank_account=user_data.bank_account,
            )
            return Response(status_code=status.HTTP_201_CREATED)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def get_author(user_id: int) -> AuthorBaseSerializer:
        try:
            author = Author.objects.get(id=user_id)
            return AuthorBaseSerializer(**dict(zip(AuthorBaseSerializer.model_fields.keys(), author)))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def update_author(user_id: int, user_data: AuthorUpdateSerializer) -> AuthorBaseSerializer:
        try:
            if Author.objects.get(id=user_id) is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            update_data = {key: value for key, value in user_data.dict().items() if value is not None}
            Author.objects.update(id=user_id, **update_data)

            return CustomerService.get_user(user_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def delete_author(user_id: int) -> Response:
        try:
            Author.objects.delete(id=user_id)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
