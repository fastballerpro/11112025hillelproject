from fastapi import Request, Depends
from apps.core.base_model import async_session_maker

async def get_data_first():
    return 30


async def get_data(request: Request, data_first=Depends(get_data_first)):
    print(request)
    return data_first + 20

async def get_session():
   async with async_session_maker() as session:
        yield session


