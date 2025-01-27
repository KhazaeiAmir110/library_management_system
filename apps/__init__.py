from fastapi import FastAPI

from apps.book.routes import router as company_router
from apps.users.routes import router as users_router

app = FastAPI()


def register_routers(app_fastapi):
    app_fastapi.include_router(users_router)
    app_fastapi.include_router(company_router)


register_routers(app)
