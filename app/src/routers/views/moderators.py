from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.src.dependencies import get_db, access_only_moderator
from app.src.models.enums import ResearchAction
from app.src.routers.services.researches import get_pending_research_by_id, get_under_review_research_by_id
from app.src.routers.schemas.researches import ResearchResponse, ResearchActionRequest

router = APIRouter(prefix="/moderators", tags=["moderators"])

@router.patch("/researches/{research_id}/", response_model=ResearchResponse)
def review_research(
    research_id: int,
    request: ResearchActionRequest,
    db: Session = Depends(get_db),
    user=Depends(access_only_moderator),
):
    
    if request.action == ResearchAction.review:
        research = get_pending_research_by_id(db, research_id)
        research.status = "UNDER_REVIEW"
        
    elif request.action == ResearchAction.publish:
        research = get_under_review_research_by_id(db, research_id)
        research.status = "PUBLISHED"
        research.is_published = True
        research.published_at = datetime.now()
        
    elif request.action == ResearchAction.reject:
        research = get_under_review_research_by_id(db, research_id)
        research.status = "REJECTED"
        research.is_published = False

    db.commit()
    return research