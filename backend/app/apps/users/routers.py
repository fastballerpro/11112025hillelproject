from fastapi import APIRouter, status, Depends

from apps.auth.password_handler import PasswordHandler
from apps.users.schemas import RegisterUserSchema, UserBaseFieldsSchemas
from apps.users.crud import user_manager
from apps.core.dependencies import get_session

users_router = APIRouter()


@users_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(user_register_data: RegisterUserSchema, session=Depends(get_session)) -> UserBaseFieldsSchemas:
    user = await user_manager.create_user(user_register_data, session)
    return user
