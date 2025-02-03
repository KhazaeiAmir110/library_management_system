from fastapi import HTTPException, status
from fastapi.responses import Response

from apps.reservation.models import Reservation
from apps.reservation.serializers import (
    ReservationCreateSerializer, ReservationBaseSerializer, ReservationUpdateSerializer
)


class ReservationService:
    @staticmethod
    def create_reservation(reservation_data: ReservationCreateSerializer) -> Response:
        try:
            Reservation.objects.create(
                customer_id=reservation_data.customer_id,
                book_id=reservation_data.book_id,
                reservation_start=reservation_data.reservation_start,
                reservation_end=reservation_data.reservation_end,
                payment=reservation_data.payment
            )
            return Response(status_code=status.HTTP_201_CREATED)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def get_reservation(reservation_id: int) -> ReservationBaseSerializer:
        try:
            reservation = Reservation.objects.get(id=reservation_id)
            return ReservationBaseSerializer(**dict(zip(ReservationBaseSerializer.model_fields.keys(), reservation)))
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def update_reservation(
            reservation_id: int, reservation_data: ReservationUpdateSerializer) -> ReservationBaseSerializer:
        try:
            if Reservation.objects.get(id=reservation_id) is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            update_data = {key: value for key, value in reservation_data.dict().items() if value is not None}
            Reservation.objects.update(id=reservation_id, **update_data)

            return ReservationService.get_reservation(reservation_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @staticmethod
    def delete_reservation(reservation_id: int) -> Response:
        try:
            Reservation.objects.delete(id=reservation_id)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
