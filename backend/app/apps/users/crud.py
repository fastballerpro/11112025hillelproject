from apps.users.schemas import RegisterUserSchema, NoteCreateSchema
from apps.auth.password_handler import PasswordHandler
from apps.users.models import User, Note
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


class NoteManager:
    async def create_note(self, session, note_data: NoteCreateSchema, user_id: int):
        query = select(Note).filter(
            Note.user_id == user_id,
            Note.name == note_data.name
        )
        result = await session.execute(query)
        maybe_note = result.scalar_one_or_none()

        if maybe_note:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f'Note with name "{note_data.name}" already exists for this user'
            )


        note = Note(
            name=note_data.name,
            content=note_data.content,
            user_id=user_id
        )

        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note

    async def get_user_notes(self, session, user_id: int):
        query = select(Note).filter(Note.user_id == user_id)
        result = await session.execute(query)
        return result.scalars().all()



user_manager = UserManager()
note_manager = NoteManager()
