from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..repositories.researches import ResearchRepository
from ..schemas.researches import ResearchesRequest
from ...dependencies import oauth2_scheme, get_db   

router = APIRouter()

@router.get("/", response_model=List[ResearchesRequest])
def research_list(
    db: Session = Depends(get_db),
    limit: int = 0,
    offset: int = 0
):
    researches = ResearchRepository.get_researches(db, limit, offset)
    return [ResearchesRequest.model_validate(research.__dict__) for research in researches]