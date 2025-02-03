from fastapi import FastAPI

from apps.core.database import Database
from apps.routes import register_routers
from base.config import DevelopmentConfig

app = FastAPI()

app.config = DevelopmentConfig()


@app.on_event("startup")
async def startup():
    from apps.book.models import Book, Genre
    from apps.reservation.models import Reservation
    from apps.users.models import User, Author, Customer, City

    User.objects.create_table()
    Customer.objects.create_table()
    Genre.objects.create_table()
    Book.objects.create_table()
    City.objects.create_table()
    Author.objects.create_table()
    Reservation.objects.create_table()


@app.middleware("http")
async def add_process_time_header(request, call_next):
    # before
    response = await call_next(request)
    # after
    return response


register_routers(app)
