from sqlalchemy.orm import relationship, Mapped

from typing import List

from app.src.database import Base
from app.src.models.annotates import intpk
from app.src.models.enums import UserRole


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[intpk]
    name: Mapped[UserRole]

    users: Mapped[List["User"]] = relationship("User", back_populates="role")
