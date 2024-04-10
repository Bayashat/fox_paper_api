from sqlalchemy.orm import relationship,Mapped

from ..database import Base
# from .user import User
from .id_abc import intpk, UserRole


class Role(Base):
    __tablename__ = "roles"
    
    id: Mapped[intpk]
    name: Mapped[str]
    
    users: Mapped[list["User"]] = relationship(back_populates="role")

