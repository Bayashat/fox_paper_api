from sqlalchemy import String, DateTime, Column, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import mapped_column, Mapped

from app.src.database import Base
# from .id_abc import IdMixin

# class File(Base):
#     __tablename__ = "file"

#     # id: Mapped[int] = mapped_column(primary_key=True)
#     # name: Mapped[str] = mapped_column(String, nullable=False)
#     # file_path: Mapped[str] = mapped_column(String, nullable=False)
#     # created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
#     # updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     file_path = Column(String, nullable=False)
#     created_at = Column(DateTime, server_default=func.now())
#     updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())