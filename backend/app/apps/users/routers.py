from fastapi import APIRouter, status

from apps.auth.password_handler import PasswordHandler
from apps.users.schemas import RegisterUserSchema, UserBaseFieldsSchema

users_router = APIRouter()


@users_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(user_register_data: RegisterUserSchema) -> UserBaseFieldsSchema:
    print(user_register_data.dict())
    p_h = await PasswordHandler.get_password_hash(user_register_data.password)
    print(p_h)

    # true case
    is_valid = await PasswordHandler.verify_password(user_register_data.password, p_h)
    print(is_valid)
    # false case
    is_valid = await PasswordHandler.verify_password("user_register_data.password", p_h)
    print(is_valid)

    return user_register_data