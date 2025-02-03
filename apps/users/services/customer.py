from fastapi import HTTPException, status, responses
from fastapi.responses import Response

from apps.users.models import Customer
from apps.users.serializers import CustomerCreateSerializer, CustomerBaseSerializer, CustomerUpdateSerializer


class CustomerService:
    @staticmethod
    def create_customer(user_data: CustomerCreateSerializer) -> Response:
        try:
            Customer.objects.create(
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
    def get_customer(user_id: int) -> CustomerBaseSerializer:
        try:
            customer = Customer.objects.get(id=user_id)
            return CustomerBaseSerializer(**dict(zip(CustomerBaseSerializer.model_fields.keys(), customer)))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def update_customer(user_id: int, user_data: CustomerUpdateSerializer) -> CustomerBaseSerializer:
        try:
            if Customer.objects.get(id=user_id) is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            update_data = {key: value for key, value in user_data.dict().items() if value is not None}
            Customer.objects.update(id=user_id, **update_data)

            return CustomerService.get_user(user_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def delete_customer(user_id: int) -> Response:
        try:
            Customer.objects.delete(id=user_id)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
