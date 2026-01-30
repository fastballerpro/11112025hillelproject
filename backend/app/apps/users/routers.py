from fastapi import APIRouter

users_router = APIRouter()


@users_router.post("/create")
async def create_user():
    return
