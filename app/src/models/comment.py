from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from ..database import Base
from .id_abc import intpk, created_at, updated_at
# from .user import User
# from .research import Research

           
class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[intpk]
    content: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at] 
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    research_id: Mapped[int] = mapped_column(ForeignKey("researches.id"), nullable=False)

    author: Mapped["User"] = relationship(back_populates="comments") 
    research: Mapped["Research"] = relationship(back_populates="comments")
    


    

    

