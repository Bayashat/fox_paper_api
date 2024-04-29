from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.src.database import Base
from app.src.models.annotates import intpk
from app.src.models.mixins import TimestampMixin
from .user import User
from .research import Research
           
class Comment(Base, TimestampMixin):
    __tablename__ = "comments"

    id: Mapped[intpk]
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    research_id: Mapped[int] = mapped_column(ForeignKey("researches.id", ondelete="CASCADE"))

    author: Mapped["User"] = relationship("User", back_populates="comments") 
    research: Mapped["Research"] = relationship("Research", back_populates="comments")
    


    

    

