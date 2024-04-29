from sqlalchemy.orm import Mapped

from app.src.models.annotates import created_at, updated_at


class TimestampMixin:
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
