from apps.book.routes import router as company_router
from apps.users.routes import router as users_router
from apps.reservation.routes import router as reservation_router


def register_routers(app_fastapi):
    app_fastapi.include_router(users_router)
    app_fastapi.include_router(company_router)
    app_fastapi.include_router(reservation_router)
