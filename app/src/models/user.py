from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import date
from typing import List

from app.src.database import Base
from app.src.models.annotates import intpk, str_256
from app.src.models.mixins import TimestampMixin
from app.src.models.enums import Gender
from .role import Role

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[intpk]
    first_name: Mapped[str_256]
    last_name: Mapped[str_256]
    email: Mapped[str] = mapped_column(String(20), index=True, unique=True)
    password: Mapped[str]
    gender: Mapped[Gender]
    phone_number: Mapped[str] = mapped_column(String(50), index=True, unique=True, nullable=True)
    date_of_birth: Mapped[date] = mapped_column(nullable=True)
    biography: Mapped[str] = mapped_column(Text, nullable=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="SET NULL"))
    
    role: Mapped["Role"] = relationship("Role", back_populates="users")
    comments: Mapped[List["Comment"]] = relationship("Comment", back_populates="author")
    research: Mapped[List["Research"]] = relationship("Research", back_populates="author")
    