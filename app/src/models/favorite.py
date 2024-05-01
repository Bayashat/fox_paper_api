from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

from app.src.database import Base
from app.src.models.annotates import intpk
from .user import User
from .research import Research


class Favorite(Base):
    __tablename__ = 'favorites'
    
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    research_id: Mapped[int] = mapped_column(ForeignKey("researches.id", ondelete="CASCADE"))
    
    user: Mapped["User"] = relationship("User", back_populates="favorites")
    research: Mapped["Research"] = relationship("Research", back_populates="favorites")
