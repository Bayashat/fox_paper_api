from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import mapped_column, Mapped

from app.src.database import Base
from sqlalchemy import Column
# from .id_abc import IdMixin

# class Category(Base):
#     __tablename__ = "category"
    
#     # id: Mapped[int] = mapped_column(primary_key=True)
#     # name = mapped_column(String, nullable=False)
#     # description = mapped_column(Text)
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     description = Column(Text)