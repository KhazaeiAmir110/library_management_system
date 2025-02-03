from fastapi import HTTPException, status, responses
from fastapi.responses import Response

from apps.users.models import User
from apps.users.serializers import UserCreateUpdateSerializer, UserBaseSerializer


class UserService:
    @staticmethod
    def create_user(user_data: UserCreateUpdateSerializer) -> Response:
        try:
            User.objects.create(
                username=user_data.username,
                password=user_data.password,
                first_name=user_data.first_name,
                last_name=user_data.last_name,
                phone=user_data.phone,
            )
            return Response(status_code=status.HTTP_201_CREATED)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def get_user(user_id: int) -> UserBaseSerializer:
        try:
            user = User.objects.get(id=user_id)
            return UserBaseSerializer(**dict(zip(UserBaseSerializer.model_fields.keys(), user)))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def update_user(user_id: int, user_data: UserCreateUpdateSerializer) -> UserBaseSerializer:
        try:
            if User.objects.get(id=user_id) is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            update_data = {key: value for key, value in user_data.dict().items() if value is not None}
            User.objects.update(id=user_id, **update_data)

            return UserService.get_user(user_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def delete_user(user_id: int) -> Response:
        try:
            User.objects.delete(id=user_id)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
