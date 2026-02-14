from fastapi import FastAPI
from apps.users.routers import users_router, note_router
from settings import settings


def get_application() -> FastAPI:
    _app = FastAPI(
        debug=settings.DEBUG
    )

    _app.include_router(users_router, prefix="/users", tags=["users"])
    _app.include_router(note_router, prefix="/notes", tags=["notes"])

    return _app


app = get_application()
