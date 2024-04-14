from fastapi import APIRouter, Depends, Response, File, UploadFile, status
from sqlalchemy.orm import Session
from typing import List

from ..repositories.researches import ResearchRepository
from ..schemas.users import UserModel
from ..schemas.researches import ResearchResponse, ResearchCreateRequest, ResearchUpdateRequest
from ..repositories.categories import CategoryRepository
from ...dependencies import get_db, access_only_user, only_authorized_user
from fastapi import HTTPException
from ..services.researches import research_create_validate, research_update_validate

router = APIRouter()

@router.get("/", response_model=List[ResearchResponse])
def research_list(
    db: Session = Depends(get_db),
    offset: int = 0,
    limit: int = 10,
    user: UserModel = Depends(only_authorized_user)
):
    researches = ResearchRepository.get_researches(db, limit, offset)
    for research in researches:
        research.category_ids = CategoryRepository.get_by_research_id(db, research.id)
        
    return [ResearchResponse.model_validate(research.__dict__) for research in researches]


# @router.post("/upload")
# def upload_research(
#     file: UploadFile = File(...),
#     db: Session = Depends(get_db)
# ):

@router.post("/", response_model=ResearchResponse, status_code=status.HTTP_201_CREATED)
def create_research(
    research: ResearchCreateRequest,
    db: Session = Depends(get_db),
    user: UserModel = Depends(access_only_user)
):
    if research_create_validate(db, research):
        db_research = ResearchRepository.create_research(db, research, user.id)

        return ResearchResponse.model_validate(db_research.__dict__)
    

@router.get("/{research_id}", response_model=ResearchResponse)
def get_research(
    research_id: int,
    db: Session = Depends(get_db),
    user: UserModel = Depends(only_authorized_user)
):
    db_research = ResearchRepository.get_by_id(db, research_id)
    db_categories = CategoryRepository.get_by_research_id(db, research_id)
    if not db_research:
        raise HTTPException(status_code=404, detail="Research not found")
    db_research.category_ids = db_categories
    return ResearchResponse.model_validate(db_research.__dict__)


@router.put("/{research_id}", response_model=ResearchUpdateRequest)
def update_research(
    research_id: int,
    research: ResearchUpdateRequest,
    db: Session = Depends(get_db),
    user: UserModel = Depends(access_only_user)
):
    db_research = research_update_validate(db, research)
    new_research = ResearchRepository.update(db, db_research, research)
    return ResearchUpdateRequest.model_validate(new_research.__dict__)


@router.delete("/{research_id}")
def delete_research(
    research_id: int,
    db: Session = Depends(get_db),
    user: UserModel = Depends(access_only_user)
):
    db_research = ResearchRepository.get_by_id(db, research_id)
    if not db_research:
        raise HTTPException(status_code=404, detail="Research not found")
    ResearchRepository.delete(db, research_id)
    return {"message": f"Research {research_id} deleted successfully"}