from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from ..database import Base
from .id_abc import intpk
    
class Category(Base):
    __tablename__ = "categories"
    
    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    
    researches: Mapped[list["Research"]] = relationship(back_populates="categories", secondary="research_categories")
    