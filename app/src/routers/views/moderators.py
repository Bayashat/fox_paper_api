from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..repositories.researches import ResearchRepository
from ...dependencies import get_db, access_only_moderator
from ..services.moderators import get_pending_researches as service_get_pending_researches, get_published_researches as service_get_published_researches
from ...models.id_abc import ResearchAction
from ..schemas.researches import ResearchResponse

router = APIRouter()


@router.get("/researches/pending", response_model=list[ResearchResponse])
def get_pending_researches(
    db: Session = Depends(get_db), user=Depends(access_only_moderator)
):
    researches = service_get_pending_researches(db)
    return researches

@router.put("/researches/{research_id}/{action}", response_model=ResearchResponse)
def review_research(
    research_id: int,
    action: ResearchAction,
    db: Session = Depends(get_db),
    user=Depends(access_only_moderator),
):
    research = ResearchRepository.get_by_id(db, research_id)
    if not research:
        raise HTTPException(status_code=404, detail="Research not found")
    
    if action == ResearchAction.review:
        research.status = "UNDER_REVIEW"
    elif action == ResearchAction.publish:
        research.status = "PUBLISHED"
        research.is_published = True
        research.published_at = datetime.now()
    elif action == ResearchAction.reject:
        research.status = "REJECTED"
        research.is_published = False

    db.commit()
    return research