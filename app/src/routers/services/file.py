from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.src.models.file import File


def check_file_exists(db: Session, file_id: int) -> File:
    if not db.query(File).filter(File.id == file_id).first():
        raise HTTPException(status_code=404, detail=f"File with id {file_id} not found")

def check_file_not_exists(db: Session, file_id: int) -> File:
    if db.query(File).filter(File.id == file_id).first():
        raise HTTPException(status_code=400, detail=f"File with id {file_id} already exists")