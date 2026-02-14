from apps.core.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class User(Base):
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    address: Mapped[str | None] = mapped_column(nullable=True)


class Note(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    name: Mapped[str]
    content: Mapped[str]