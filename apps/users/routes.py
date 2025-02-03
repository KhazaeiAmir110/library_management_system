from typing import List

from fastapi import APIRouter, HTTPException, status

from apps.users.models import Users, Author, Customer
from apps.users.serializers import (
    UserCreateSerializer, UserBaseSerializer, UserUpdateSerializer,
    CustomerCreateSerializer, CustomerBaseSerializer, CustomerUpdateSerializer,
    AuthorCreateSerializer, AuthorBaseSerializer, AuthorUpdateSerializer
)
from apps.users.services import UserService, CustomerService, AuthorService

router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/")
async def create_user(user: UserCreateSerializer, status_code=201):
    return UserService.create_user(user)


@router.get("/", response_model=List[UserBaseSerializer])
async def list_users():
    try:
        users = Users.objects.all()
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
async def update_user(user_id: int, user: UserUpdateSerializer, status_code=200):
    return UserService.update_user(user_id, user)


@router.delete("/{user_id}")
async def delete_user(user_id: int, status_code=200):
    return UserService.delete_user(user_id)


@router.post("/customer")
async def create_customer(user: CustomerCreateSerializer, status_code=201):
    return CustomerService.create_customer(user)


@router.get("/", response_model=List[CustomerBaseSerializer])
async def list_customers():
    try:
        customers = Customer.objects.all()
        customer_list = [
            UserBaseSerializer(**{
                field_name: field_value
                for field_name, field_value in zip(UserBaseSerializer.__fields__.keys(), customer)
            })
            for customer in customers
        ]
        return customer_list
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/customer/{customer_id}", response_model=CustomerBaseSerializer)
async def get_customer(user_id: int, status_code=200):
    user = CustomerService.get_customer(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@router.patch("/customer/{customer_id}")
async def update_customer(user_id: int, user: CustomerUpdateSerializer, status_code=200):
    return CustomerService.update_customer(user_id, user)


@router.delete("/customer/{customer_id}")
async def delete_customer(user_id: int, status_code=200):
    return CustomerService.delete_customer(user_id)


@router.post("/author")
async def create_author(user: AuthorCreateSerializer, status_code=201):
    return AuthorService.create_author(user)


@router.get("/author", response_model=List[AuthorBaseSerializer])
async def list_authors():
    try:
        authors = Author.objects.all()
        author_list = [
            AuthorBaseSerializer(**{
                field_name: field_value
                for field_name, field_value in zip(UserBaseSerializer.__fields__.keys(), author)
            })
            for author in authors
        ]
        return author_list
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/author/{author_id}", response_model=AuthorBaseSerializer)
async def get_author(user_id: int, status_code=200):
    user = AuthorService.get_author(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@router.patch("/author/{author_id}")
async def update_author(user_id: int, user: AuthorUpdateSerializer, status_code=200):
    return AuthorService.update_author(user_id, user)


@router.delete("/author/{author_id}")
async def delete_author(user_id: int, status_code=200):
    return AuthorService.delete_author(user_id)
