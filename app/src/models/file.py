from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.src.database import Base
from app.src.models.annotates import intpk, str_256
from app.src.models.mixins import TimestampMixin

class File(Base, TimestampMixin):
    __tablename__ = "files"

    id: Mapped[intpk]
    file_path: Mapped[str_256] = mapped_column(unique=True)
    
    research: Mapped["Research"] = relationship("Research", back_populates="files")
    