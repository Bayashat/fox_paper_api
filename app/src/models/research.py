from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from datetime import datetime

from ..database import Base
from .id_abc import intpk, Status, created_at, updated_at

from .category import Category
from .comment import Comment
from .file import File
    
class Research(Base):
    __tablename__ = "researches"
    
    id: Mapped[intpk]
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[Status]
    is_published: Mapped[bool]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at] 
    published_at: Mapped[datetime]
    file_id: Mapped[int] = mapped_column(ForeignKey("files.id"))
    
    
    categories: Mapped[list["Category"]] = relationship(back_populates="researches", secondary="research_categories")
    authors: Mapped[list["User"]] = relationship(back_populates="researches", secondary="research_authors")
    comments: Mapped[list["Comment"]] = relationship(back_populates="research")
    files: Mapped["File"] = relationship(back_populates="research")



class ResearchCategories(Base):
    __tablename__ = 'research_categories'
    
    research_id: Mapped[int] = mapped_column(ForeignKey("researches.id", ondelete="SET NULL"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="SET NULL"), primary_key=True)
