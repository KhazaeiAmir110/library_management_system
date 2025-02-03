from typing import List

from fastapi import APIRouter, HTTPException, status

from apps.users.models import User
from apps.users.serializers import UserCreateUpdateSerializer, UserBaseSerializer
from apps.users.services import UserService

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/")
async def create_user(user: UserCreateUpdateSerializer, status_code=201):
    return UserService.create_user(user)


@router.get("/", response_model=List[UserBaseSerializer])
async def list_users():
    try:
        users = User.objects.all()
        user_list = [
            UserBaseSerializer(**{
                field_name: field_value
                for field_name, field_value in zip(UserBaseSerializer.__fields__.keys(), book)
            })
            for book in users
        ]
        return user_list
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{user_id}", response_model=UserBaseSerializer)
async def get_user(user_id: int, status_code=200):
    user = UserService.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@router.patch("/{user_id}")
async def update_user(user_id: int, user: UserCreateUpdateSerializer, status_code=200):
    return UserService.update_user(user_id, user)


@router.delete("/{user_id}")
async def delete_user(user_id: int, status_code=200):
    return UserService.delete_user(user_id)
