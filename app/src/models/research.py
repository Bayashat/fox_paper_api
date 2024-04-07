from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from datetime import datetime

from ..database import Base
from .id_abc import intpk, Status, created_at, updated_at
# from .user import User
# from .file import File
# from .category import Category
# from .comment import Comment


    
class Research(Base):
    __tablename__ = "researches"
    
    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[Status] = mapped_column(nullable=False)
    is_published: Mapped[bool] = mapped_column(default=False, nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at] 
    published_at: Mapped[datetime] = mapped_column(nullable=False)
    file_id: Mapped[int] = mapped_column(ForeignKey("files.id"), nullable=False)
    
    
    categories: Mapped[list["Category"]] = relationship(back_populates="researches", secondary="research_categories")
    authors: Mapped[list["User"]] = relationship(back_populates="researches", secondary="research_authors")
    comments: Mapped[list["Comment"]] = relationship(back_populates="research")
    files: Mapped["File"] = relationship(back_populates="research")



class ResearchCategories(Base):
    __tablename__ = 'research_categories'
    
    research_id: Mapped[int] = mapped_column(ForeignKey("researches.id", ondelete="SET NULL"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="SET NULL"), primary_key=True)
