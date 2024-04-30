from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.src.models.file import File
from app.src.models.research import Research


def check_file_not_exists(db: Session, file_id: int):
    if not db.query(File).filter(File.id == file_id).first():
        raise HTTPException(status_code=404, detail=f"File with id {file_id} not found")
    if db.query(Research).filter(Research.file_id == file_id).first():
        raise HTTPException(status_code=400, detail=f"File with id {file_id} already exists in a research")
