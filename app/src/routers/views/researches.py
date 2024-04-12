from fastapi import APIRouter, Depends, Response, File, UploadFile, status
from sqlalchemy.orm import Session
from typing import List

from ..repositories.researches import ResearchRepository
from ..schemas.users import UserModel
from ..schemas.researches import ResearchResponse, ResearchCreateRequest, ResearchUpdateRequest
from ...dependencies import get_db, access_only_researcher
from fastapi import HTTPException

router = APIRouter()

@router.get("/", response_model=List[ResearchResponse])
def research_list(
    db: Session = Depends(get_db),
    offset: int = 0,
    limit: int = 10,
):
    researches = ResearchRepository.get_researches(db, limit, offset)
    return [ResearchResponse.model_validate(research.__dict__) for research in researches]


# @router.post("/upload")
# def upload_research(
#     file: UploadFile = File(...),
#     db: Session = Depends(get_db)
# ):

@router.post("/")
def create_research(
    research: ResearchCreateRequest,
    db: Session = Depends(get_db),
    # user: UserModel = Depends(access_only_researcher)
):
    db_research = ResearchRepository.create_research(db, research)
    return ResearchResponse.model_validate(db_research.__dict__)
    

@router.get("/{research_id}", response_model=ResearchResponse)
def get_research(
    research_id: int,
    db: Session = Depends(get_db)
):
    db_research = ResearchRepository.get_by_id(db, research_id)
    if not db_research:
        raise HTTPException(status_code=404, detail="Research not found")
    return ResearchResponse.model_validate(db_research.__dict__)


@router.put("/{research_id}", response_model=ResearchUpdateRequest)
def update_research(
    research_id: int,
    research: ResearchUpdateRequest,
    db: Session = Depends(get_db),
    # user: UserModel = Depends(access_only_researcher)
):
    db_research = ResearchRepository.get_by_id(db, research_id)
    if not db_research:
        raise HTTPException(status_code=404, detail="Research not found")
    new_research = ResearchRepository.update(db, db_research, research)
    return ResearchUpdateRequest.model_validate(new_research.__dict__)

@router.delete("/{research_id}")
def delete_research(
    research_id: int,
    db: Session = Depends(get_db),
    user: UserModel = Depends(access_only_researcher)
):
    db_research = ResearchRepository.get_by_id(db, research_id)
    if not db_research:
        raise HTTPException(status_code=404, detail="Research not found")
    ResearchRepository.delete(db, research_id)
    return {"message": f"Research {research_id} deleted successfully"}