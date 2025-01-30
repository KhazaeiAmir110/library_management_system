from fastapi import FastAPI

from apps.book.routes import router as company_router
from apps.core.database import Database
from apps.users.routes import router as users_router
from config import DevelopmentConfig

app = FastAPI()

app.config = DevelopmentConfig()


@app.on_event("startup")
async def startup():
    from apps.book.models import Book, City, Genre, Author
    from apps.reservation.models import Reservation
    from apps.users.models import User

    User.objects.create_table()
    Author.objects.create_table()
    City.objects.create_table()
    Genre.objects.create_table()
    Book.objects.create_table()
    Reservation.objects.create_table()

    print(City.objects.all())


def register_routers(app_fastapi):
    app_fastapi.include_router(users_router)
    app_fastapi.include_router(company_router)


register_routers(app)
