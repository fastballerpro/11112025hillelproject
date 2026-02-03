from fastapi import APIRouter, status

from apps.auth.password_handler import PasswordHandler
from apps.users.schemas import RegisterUserSchema, UserBaseFieldsSchemas


users_router = APIRouter()


@users_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(user_register_data: RegisterUserSchema) -> UserBaseFieldsSchemas:
    return user_register_data
