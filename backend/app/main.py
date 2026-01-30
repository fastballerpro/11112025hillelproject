from fastapi import FastAPI
from apps.users.routers import users_router


def get_application() -> FastAPI:
    _app = FastAPI()

    _app.include_router(users_router, prefix="/users", tags=["users"])

    return _app


app = get_application()
