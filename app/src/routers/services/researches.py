from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas.researches import ResearchCreateRequest
from ..repositories.researches import ResearchRepository


def research_create_validate(db: Session, research: ResearchCreateRequest):
    file = ResearchRepository.get_by_file_id(db, research.file_id)
    if file:
        # error for such file already exists
        raise HTTPException(status_code=400, detail="File already exists")
    return True


def research_update_validate(db: Session, research: ResearchCreateRequest):
    existing_research = ResearchRepository.get_by_file_id(db, research.file_id)
    if not existing_research:
        raise HTTPException(status_code=404, detail="Research not found")
    if ResearchRepository.get_by_file_id(db, research.file_id):
        raise HTTPException(status_code=400, detail="File already exists")
    return existing_research    