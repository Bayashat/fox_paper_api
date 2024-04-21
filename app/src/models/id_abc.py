from datetime import datetime
from enum import Enum
from typing_extensions import Annotated
from sqlalchemy import func, text
from sqlalchemy.orm import mapped_column

intpk = Annotated[int, mapped_column(primary_key=True)]

# created_at: Mapped[datetime] = mapped_column(server_default=func.now())
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=text("TIMEZONE('utc', now())"))]


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
    PREFER_NOT_TO_SAY = "Prefer not to say"  

# create type user_role as ENUM('USER', 'MODERATOR');

class UserRole(Enum):
    USER = "User"
    MODERATOR = "Moderator"

class Status(Enum):
    SUBMITTED = "Submitted"
    UNDER_REVIEW = "Under Review"
    REJECTED = "Rejected"
    PUBLISHED = "Published"


class ResearchAction(str, Enum):
    review = "review"
    publish = "publish"
    reject = "reject"