from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

from ..database import Base
from .id_abc import intpk, Gender, created_at, updated_at

from .role import Role

class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    gender: Mapped[Gender]
    phone_number: Mapped[str] = mapped_column(unique=True, nullable=True)
    date_of_birth: Mapped[date] = mapped_column(nullable=True)
    biography: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="SET NULL"))
    
    role: Mapped["Role"] = relationship(back_populates="users")
    comments: Mapped[list["Comment"]] = relationship(back_populates="author")
    