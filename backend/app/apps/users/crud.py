from apps.users.schemas import RegisterUserSchema
from apps.auth.password_handler import PasswordHandler
from apps.users.models import User
from sqlalchemy import select
from fastapi import HTTPException, status


class UserManager:
    async def create_user(self, session, user_register_data: RegisterUserSchema):
        maybe_user = await self.get(session=session, user_email=user_register_data.email)
        if maybe_user:
           raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'User with email {user_register_data.email} already exists')
        
        hashed_password = await PasswordHandler.get_password_hash(user_register_data.password)
        user = User(
            name=user_register_data.name,
            email=user_register_data.email,
            hashed_password=hashed_password,
        )
        session.add(user)
        await session.commit()
        return user
    
    async def get(self, session, user_email) -> User | None:
        query = select(User).filter(User.email == user_email)
        result = await session.execute(query)
        return result.scalar_one_or_none()


user_manager = UserManager()
