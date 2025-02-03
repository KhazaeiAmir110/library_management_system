import uuid
from typing import Literal, Optional

from apps.users.models import User
from pydantic import BaseModel, validator, Field


class UserBaseSerializer(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    phone: str


class UserCreateUpdateSerializer(BaseModel):
    first_name: str = Field(min_length=1, max_length=50, description="User's first name")
    last_name: str = Field(min_length=1, max_length=50, description="User's last name")
    username: str = Field(min_length=3, max_length=30, description="Unique username for the user")
    password: str = Field(min_length=8, description="User's password")
    phone: str = Field(min_length=10, max_length=15, description="User's phone number")

    @validator("username")
    def validate_username(cls, value):
        # Here you would check if the username already exists in the database
        if User.objects.filter(username=value).exists():
            raise ValueError("Username already exists")
        return value

    @validator("phone")
    def validate_phone(cls, value):
        # Here you would check if the phone number already exists in the database
        if User.objects.filter(phone=value).exists():
            raise ValueError("Phone number already exists")
        return value

    @validator("password")
    def validate_password(cls, value):
        # Here you could implement more complex password rules if necessary
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value
