from typing import List

from fastapi import APIRouter, HTTPException, status

from apps.reservation.models import Reservation
from apps.reservation.serializers import (
    ReservationBaseSerializer, ReservationCreateSerializer, ReservationUpdateSerializer
)
from apps.reservation.services import ReservationService

router = APIRouter(prefix="/reservation", tags=["Reservation"])


@router.post("/")
async def create_reservation(reservation: ReservationCreateSerializer, status_code=201):
    return ReservationService.create_reservation(reservation)


@router.get("/", response_model=List[ReservationBaseSerializer])
async def list_reservation():
    try:
        reservations = Reservation.objects.all()
        reservation_list = [
            ReservationBaseSerializer(**{
                field_name: field_value
                for field_name, field_value in zip(ReservationBaseSerializer.__fields__.keys(), reservation)
            })
            for reservation in reservations
        ]
        return reservation_list
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{reservation_id}", response_model=ReservationBaseSerializer)
async def get_reservation(reservation_id: int, status_code=200):
    reservation = ReservationService.get_reservation(reservation_id)
    if reservation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return reservation


@router.patch("/{reservation_id}")
async def update_reservation(reservation_id: int, reservation: ReservationUpdateSerializer, status_code=200):
    return ReservationService.update_reservation(reservation_id, reservation)


@router.delete("/{reservation_id}")
async def delete_reservation(reservation_id: int, status_code=200):
    return ReservationService.delete_reservation(reservation_id)
