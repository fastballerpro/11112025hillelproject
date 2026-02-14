from fastapi import APIRouter, status, Depends

from apps.users.schemas import RegisterUserSchema, UserResponseSchema, NoteResponseSchema, NoteCreateSchema
from apps.users.crud import user_manager, note_manager
from apps.core.dependencies import get_session

users_router = APIRouter()
note_router = APIRouter()

@users_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(user_register_data: RegisterUserSchema, session=Depends(get_session)) -> UserResponseSchema:
    user = await user_manager.create_user(user_register_data=user_register_data, session=session)
    return user

@note_router.post('/create_note', status_code=status.HTTP_201_CREATED)
async def create_note(note_data: NoteCreateSchema, user_id: int, session=Depends(get_session)) -> NoteResponseSchema:
    note = await note_manager.create_note(note_data=note_data, session=session, user_id=user_id)
    return note