from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.src.models.research import Research
from app.src.models.enums import Status
from app.src.routers.schemas.researches import ResearchCreateRequest
from app.src.routers.services.file import check_file_not_exists
from app.src.routers.services.category import check_category_ids_valid

def research_create_validate(db: Session, research: ResearchCreateRequest):
    check_file_not_exists(db, research.file_id)
    check_category_ids_valid(db, research.category_ids)

def check_reserach_exists(db: Session, research_id: int):
    if not db.query(Research).filter(Research.id == research_id, Research.status == Status.PUBLISHED).first():
        raise HTTPException(status_code=404, detail="Research not found")


def get_pending_research_by_id(db: Session, research_id: int):
    research = db.query(Research).filter(Research.status == Status.SUBMITTED, Research.id == research_id).first()
    if not research:
        raise HTTPException(status_code=404, detail="Research not found")
    return research
    

def get_under_review_research_by_id(db: Session, research_id: int):
    research = db.query(Research).filter(Research.status == Status.UNDER_REVIEW, Research.id == research_id).first()
    if not research:
        raise HTTPException(status_code=404, detail="Research not found")
    return research
