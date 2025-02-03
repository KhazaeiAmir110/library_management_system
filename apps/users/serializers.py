from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator, Field

from apps.users.models import Users


class UserBaseSerializer(BaseModel):
    id: int
    password: str
    is_superuser: bool
    is_active: bool
    first_name: str
    last_name: str
    date_joined: datetime
    username: str
    phone: str
    otp: Optional[int] = None


class UserCreateSerializer(BaseModel):
    first_name: str = Field(min_length=1, max_length=50, description="Users's first name")
    last_name: str = Field(min_length=1, max_length=50, description="Users's last name")
    username: str = Field(min_length=3, max_length=30, description="Unique username for the user")
    password: str = Field(min_length=8, description="Users's password")
    phone: str = Field(min_length=10, max_length=15, description="Users's phone number")

    @validator("username")
    def validate_username(cls, value):
        if Users.objects.get(username=value):
            raise ValueError("Username already exists")
        return value

    @validator("phone")
    def validate_phone(cls, value):
        if Users.objects.get(phone=value):
            raise ValueError("Phone number already exists")
        return value

    @validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value


class UserUpdateSerializer(BaseModel):
    first_name: str = Field(min_length=1, max_length=50, description="Users's first name", default=None)
    last_name: str = Field(min_length=1, max_length=50, description="Users's last name", default=None)
    username: str = Field(min_length=3, max_length=30, description="Unique username for the user", default=None)
    password: str = Field(min_length=8, description="Users's password", default=None)
    phone: str = Field(min_length=10, max_length=15, description="Users's phone number", default=None)

    @validator("username")
    def validate_username(cls, value):
        if Users.objects.get(username=value):
            raise ValueError("Username already exists")
        return value

    @validator("phone")
    def validate_phone(cls, value):
        if Users.objects.get(phone=value):
            raise ValueError("Phone number already exists")
        return value

    @validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value


class CustomerBaseSerializer(BaseModel):
    pass


class CustomerCreateSerializer(BaseModel):
    pass


class CustomerUpdateSerializer(BaseModel):
    pass


class AuthorBaseSerializer(BaseModel):
    pass


class AuthorCreateSerializer(BaseModel):
    pass


class AuthorUpdateSerializer(BaseModel):
    pass
