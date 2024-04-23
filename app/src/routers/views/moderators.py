from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..repositories.researches import ResearchRepository
from ..repositories.categories import CategoryRepository
from ...dependencies import get_db, access_only_moderator
from ..services.researches import get_pending_research_by_id, get_under_review_research_by_id
from ..services.moderators import get_pending_researches as service_get_pending_researches, get_published_researches as service_get_published_researches
from ...models.id_abc import ResearchAction
from ..schemas.researches import ResearchResponse

router = APIRouter()

# write 1 api for 3: pending, under-review, rejected
@router.get("/researches/{status}", response_model=list[ResearchResponse])
def get_researches_by_status(
    status: str,
    db: Session = Depends(get_db),
    user=Depends(access_only_moderator),
):
    researches = ResearchRepository.get_by_status(db, status)
    if not researches:
        raise HTTPException(status_code=404, detail=f"No researches {status}")
    for research in researches:
        research.category_ids = CategoryRepository.get_by_research_id(db, research.id)
    return researches


# @router.get("/researches/pending", response_model=list[ResearchResponse])
# def get_pending_researches(
#     db: Session = Depends(get_db), user=Depends(access_only_moderator)
# ):
#     researches = service_get_pending_researches(db)
#     for research in researches:
#         research.category_ids = CategoryRepository.get_by_research_id(db, research.id)
#     return researches


# @router.get("/researches/under-review", response_model=list[ResearchResponse])
# def get_under_review_researches(
#     db: Session = Depends(get_db), user=Depends(access_only_moderator)
# ):
#     researches = ResearchRepository.get_under_review(db)
#     if not researches:
#         raise HTTPException(status_code=404, detail="No researches under review")
#     for research in researches:
#         research.category_ids = CategoryRepository.get_by_research_id(db, research.id)
#     return researches

# @router.get("/researches/rejected", response_model=list[ResearchResponse])
# def get_rejected_researches(
#     db: Session = Depends(get_db), user=Depends(access_only_moderator)
# ):
#     researches = ResearchRepository.get_rejected(db)
#     if not researches:
#         raise HTTPException(status_code=404, detail="No researches rejected")
#     for research in researches:
#         research.category_ids = CategoryRepository.get_by_research_id(db, research.id)
#     return researches

@router.put("/researches/{research_id}/{action}", response_model=ResearchResponse)
def review_research(
    research_id: int,
    action: ResearchAction,
    db: Session = Depends(get_db),
    user=Depends(access_only_moderator),
):
    
    if action == ResearchAction.review:
        research = get_pending_research_by_id(db, research_id)
        research.status = "UNDER_REVIEW"
        
    elif action == ResearchAction.publish:
        research = get_under_review_research_by_id(db, research_id)
        research.status = "PUBLISHED"
        research.is_published = True
        research.published_at = datetime.now()
    elif action == ResearchAction.reject:
        research = get_under_review_research_by_id(db, research_id)
        research.status = "REJECTED"
        research.is_published = False

    db.commit()
    return research