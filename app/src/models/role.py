from sqlalchemy import String, Integer
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.src.database import Base
from sqlalchemy import Column

# class Role(Base):
#     __tablename__ = "role"

#     # id: Mapped[int] = mapped_column(primary_key=True)
#     # name: Mapped[str] = mapped_column(String, unique=True, nullable=False)'
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String, unique=True, nullable=False)
    
#     users = relationship("User", back_populates="role")
