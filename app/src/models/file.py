from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime

from ..database import Base
from .id_abc import intpk
# from .research import Research

class File(Base):
    __tablename__ = "files"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(nullable=False)
    file_path: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime] 
    
    research: Mapped["Research"] = relationship(back_populates="files")
    