from fastapi import FastAPI
from apps.users.routers import users_router


def get_application() -> FastAPI:
    app = FastAPI()

    app.include_router(
        users_router,
        prefix="/users",
        tags=["users"],
    )

    return app


app = get_application()
