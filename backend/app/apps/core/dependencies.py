from fastapi import Request, Depends
from apps.core.base_model import async_session_maker

async def get_session():
   async with async_session_maker() as session:
        yield session

