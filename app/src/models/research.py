from sqlalchemy import Boolean, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql import func

from app.src.database import Base
from sqlalchemy import Column
# from .id_abc import IdMixin
# from .category import Category
# from .user import ResearchAuthors
# from .comment import Comment

# class Research(Base):
#     __tablename__ = "research"
    
#     # id: Mapped[int] = mapped_column(primary_key=True)
#     # title: Mapped[str] = mapped_column(String, nullable=False)
#     # description: Mapped[str] = mapped_column(Text)
#     # file_id: Mapped[int] = mapped_column(Integer, ForeignKey("file.id"), nullable=False)
#     # status: Mapped[int] = mapped_column(Integer, nullable=False)
#     # created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
#     # updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
#     # published_at: Mapped[DateTime] = mapped_column(DateTime)
#     # is_published: Mapped[bool] = mapped_column(Boolean, default=False)
    
#     id = Column(Integer, primary_key=True)
#     title = Column(String, nullable=False)
#     description = Column(Text)
#     status = Column(Integer, nullable=False)
#     created_at = Column(DateTime, server_default=func.now())
#     updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
#     published_at = Column(DateTime)
#     is_published = Column(Boolean, default=False)
#     file_id = Column(Integer, ForeignKey("file.id"), nullable=False)
    
#     categories = relationship("Category", back_populates="research")
#     authors = relationship("ResearchAuthors", back_populates="research")
#     comments = relationship("Comment", back_populates="research")
    