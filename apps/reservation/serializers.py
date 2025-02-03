from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ReservationBaseSerializer(BaseModel):
    id: int
    customer_id: int
    book_id: int
    reservation_start: Optional[datetime] = None
    reservation_end: Optional[datetime] = None
    payment: Optional[float] = None


class ReservationCreateSerializer(BaseModel):
    pass


class ReservationUpdateSerializer(BaseModel):
    pass
