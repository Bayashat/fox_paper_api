from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import relationship, mapped_column, Mapped

from datetime import datetime
from typing import List

from app.src.database import Base
from app.src.models.annotates import intpk, str_256
from app.src.models.mixins import TimestampMixin
from app.src.models.enums import Status
from .file import File
from .user import User
    
class Research(Base, TimestampMixin):
    __tablename__ = "researches"
    
    id: Mapped[intpk]
    title: Mapped[str_256]
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[Status] = mapped_column(nullable=True, default=Status.SUBMITTED)
    published_at: Mapped[datetime] = mapped_column(nullable=True)
    file_id: Mapped[int] = mapped_column(ForeignKey("files.id", ondelete="CASCADE"), unique=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    
    categories: Mapped[List["Category"]] = relationship(back_populates="researches", secondary="research_categories")
    comments: Mapped[List["Comment"]] = relationship("Comment", back_populates="research")
    files: Mapped["File"] = relationship("File", back_populates="research")
    author: Mapped["User"] = relationship("User", back_populates="research")
    favorites: Mapped[List["Favorite"]] = relationship("Favorite", back_populates="research")

class ResearchCategories(Base):
    __tablename__ = 'research_categories'
    
    research_id: Mapped[int] = mapped_column(ForeignKey("researches.id", ondelete="CASCADE"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"), primary_key=True)