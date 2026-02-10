from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from datetime import datetime
from sqlalchemy.sql import func
from settings import settings



class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())

    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'
    
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=10
)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)