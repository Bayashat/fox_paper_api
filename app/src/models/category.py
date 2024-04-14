from sqlalchemy.orm import Mapped, relationship

from ..database import Base
from .id_abc import intpk
    
class Category(Base):
    __tablename__ = "categories"
    
    id: Mapped[intpk]
    name: Mapped[str]
    
    researches: Mapped[list["Research"]] = relationship(back_populates="categories", secondary="research_categories")