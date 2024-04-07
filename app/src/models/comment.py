from sqlalchemy import Column, ForeignKey, Integer, Text, DateTime, func
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.src.database import Base
# from .id_abc import IdMixin
# from .user import User
# from .research import Research



# class Comment(Base):
#     __tablename__ = "comment"

#     # id: Mapped[int] = mapped_column(primary_key=True)
#     # content: Mapped[str] = mapped_column(Text, nullable=False)
#     # created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
#     # updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
#     # user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
#     # research_id: Mapped[int] = mapped_column(Integer, ForeignKey("research.id"), nullable=False)
    

#     id = Column(Integer, primary_key=True)
#     content = Column(Text, nullable=False)
#     created_at = Column(DateTime, server_default=func.now())
#     updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     research_id = Column(Integer, ForeignKey("research.id"), nullable=False)
    
#     author = relationship("User", back_populates="comments")
#     research = relationship("Research", back_populates="comments")
    