from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..repositories.researches import ResearchRepository
from ..repositories.categories import CategoryRepository
from ...dependencies import get_db, access_only_moderator
from ..services.researches import get_pending_research_by_id, get_under_review_research_by_id
from ..services.moderators import get_pending_researches as service_get_pending_researches, get_published_researches as service_get_published_researches
from ...models.enums import ResearchAction
from ..schemas.researches import ResearchResponse, ResearchActionRequest

router = APIRouter()

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