from fastapi import HTTPException, UploadFile

from sqlalchemy.orm import Session

import uuid
import aiofiles
from werkzeug.utils import secure_filename

from app.src.models.file import File
from app.src.models.research import Research
from app.src.routers.repositories.file import FileRepository


def check_file_exists(db: Session, file_id: int):
    if not db.query(File).filter(File.id == file_id).first():
        raise HTTPException(status_code=404, detail=f"File with id {file_id} not found")
    if db.query(Research).filter(Research.file_id == file_id).first():
        raise HTTPException(status_code=400, detail=f"File with id {file_id} already exists in a research")


async def save_uploaded_file(db: Session, file: UploadFile) -> dict:
    if file.content_type not in ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        raise HTTPException(status_code=400, detail="File type not allowed")

    # use uuid and secure_filename to avoid file name conflicts and security issues
    file_name = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4()}-{file_name}"
    file_path = f"app/src/uploads/{unique_filename}"

    async with aiofiles.open(file_path, "wb") as buffer:
        await buffer.write(await file.read())

    file_id = FileRepository.save_file(db, file_path)

    return {"file_id": file_id, "file_path": file_path, "message": "File uploaded successfully"}