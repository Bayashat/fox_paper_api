from sqlalchemy.orm import Session

from app.src.models.file import File
from app.src.routers.services.db import add_commit_refresh


class FileRepository:
    @staticmethod
    def save_file(db: Session, file_path: str) -> int:
        new_file = File(file_path=file_path)
        add_commit_refresh(db, new_file)
        return new_file.id
        