from sqlalchemy.orm import Mapped, relationship

from typing import List

from app.src.database import Base
from app.src.models.annotates import intpk, str_256

    
class Category(Base):
    __tablename__ = "categories"
    
    id: Mapped[intpk]
    name: Mapped[str_256]
    
    researches: Mapped[List["Research"]] = relationship(back_populates="categories", secondary="research_categories")