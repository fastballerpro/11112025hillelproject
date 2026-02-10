from apps.users.schemas import RegisterUserSchema, UserBaseFieldsSchemas
from apps.auth.password_handler import PasswordHandler
from apps.users.models import User



class UserManager:
    async def create_user(self, session, user_register_data: RegisterUserSchema):
        hashed_password = await PasswordHandler.get_password_hash(user_register_data.password)
        user = User(
            name=user_register_data.name,
            email=user_register_data.email,
            hashed_password=hashed_password,
        )
        session.add(user)
        await session.commit()
        return user
    

user_manager = UserManager()
