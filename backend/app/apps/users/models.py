from apps.core.base_model import Base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class User(Base):
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    