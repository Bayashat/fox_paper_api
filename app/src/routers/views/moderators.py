from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ...models.research import Research
from ..repositories.researches import ResearchRepository
from ...dependencies import get_db, access_only_moderator
from ..services.moderators import get_pending_researches as service_get_pending_researches, get_published_researches as service_get_published_researches

router = APIRouter()


@router.get("/researches/pending")
def get_pending_researches(
    db: Session = Depends(get_db), user=Depends(access_only_moderator)
):
    researches = service_get_pending_researches(db)
    return researches

@router.put("/researches/{research_id}/review")
def review_research(
    research_id: int,
    db: Session = Depends(get_db),
    user=Depends(access_only_moderator),
):
    research = ResearchRepository.get_by_id(db, research_id)
    if not research:
        raise HTTPException(status_code=404, detail="Research not found")
    research.status = "UNDER_REVIEW"
    db.commit()
    return research


@router.put("/researches/{research_id}/publish")
def publish_research(
    research_id: int,
    db: Session = Depends(get_db),
    user=Depends(access_only_moderator),
):
    research = ResearchRepository.get_by_id(db, research_id)
    if not research:
        raise HTTPException(status_code=404, detail="Research not found")
    research.status = "PUBLISHED"
    db.commit()
    return research

@router.put("/researches/{research_id}/reject")
def reject_research(
    research_id: int,
    db: Session = Depends(get_db),
    user=Depends(access_only_moderator),
):
    research = ResearchRepository.get_by_id(db, research_id)
    if not research:
        raise HTTPException(status_code=404, detail="Research not found")
    research.status = "REJECTED"
    db.commit()
    return research


@router.get("/researches/published")
def get_published_researches(
    db: Session = Depends(get_db), user=Depends(access_only_moderator)
):
    researches = service_get_published_researches(db)
    return researches


@router.delete("/researches/{research_id}")
def delete_research(
    research_id: int,
    db: Session = Depends(get_db),
    user=Depends(access_only_moderator),
):
    research = ResearchRepository.get_by_id(db, research_id)
    if not research:
        raise HTTPException(status_code=404, detail="Research not found")
    db.delete(research)
    db.commit()
    return {"message": "Research deleted successfully"}