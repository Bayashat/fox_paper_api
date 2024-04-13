from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime

from ..database import Base
from .id_abc import intpk, created_at, updated_at

class File(Base):
    __tablename__ = "files"

    id: Mapped[intpk]
    file_path: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at] 
    
    research: Mapped["Research"] = relationship(back_populates="files")
    