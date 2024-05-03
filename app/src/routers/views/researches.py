from fastapi import APIRouter, Depends, status, UploadFile

from sqlalchemy.orm import Session

from typing import List

from app.src.dependencies import get_db, access_only_user, only_authorized_user, validate_file_size
from app.src.models.enums import Status
from app.src.routers.repositories.researches import ResearchRepository
from app.src.routers.repositories.categories import CategoryRepository
from app.src.routers.schemas.users import UserModel
from app.src.routers.schemas.researches import (
    ResearchResponse,
    ResearchCreateRequest,
    ResearchUpdateRequest,
)
from app.src.routers.services.researches import research_create_validate
from app.src.routers.services.researches import check_reserach_exists
from app.src.routers.services.users import check_user_validate_by_researchID
from app.src.routers.services.file import save_uploaded_file


router = APIRouter(prefix="/researches", tags=["researches"])


@router.get("/", response_model=List[ResearchResponse])
def research_list(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 20,
    search_text: str | None = None,
    author: str | None = None,
    category_ids: str | None = None,
    status: Status | None = None,
    user: UserModel = Depends(only_authorized_user),
):
    if user.role_id == 2:
        researches = ResearchRepository.get_researches(
            db, limit, skip, search_text, author, category_ids, status
        )
    else:
        researches = ResearchRepository.get_researches(
            db, limit, skip, search_text, author, category_ids, Status.PUBLISHED
        )
    for research in researches:
        research.category_ids = CategoryRepository.get_by_research_id(db, research.id)

    return [ResearchResponse.model_validate(research.__dict__) for research in researches]

@router.post("/upload-file", status_code=status.HTTP_201_CREATED)  
async def upload_file(
    file: UploadFile = Depends(validate_file_size),
    db: Session = Depends(get_db),
):
    result = await save_uploaded_file(db, file)
    return result
    
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ResearchResponse)
def create_research(
    research_data: ResearchCreateRequest,
    db: Session = Depends(get_db),
    user: UserModel = Depends(access_only_user),
):
    research_create_validate(db, research_data)
    db_research = ResearchRepository.create_research(db, research_data, user.id)
    db_category_ids = CategoryRepository.get_by_research_id(db, db_research.id)
    db_research.category_ids = db_category_ids

    return ResearchResponse.model_validate(db_research.__dict__)



@router.get("/{research_id}", status_code=status.HTTP_200_OK, response_model=ResearchResponse)
def get_research(
    research_id: int, db: Session = Depends(get_db), user: UserModel = Depends(only_authorized_user)
):
    check_reserach_exists(db, research_id)
    db_research = ResearchRepository.get_by_id(db, research_id)
    db_category_ids = CategoryRepository.get_by_research_id(db, research_id)

    db_research.category_ids = db_category_ids
    return ResearchResponse.model_validate(db_research.__dict__)


@router.patch("/{research_id}", response_model=ResearchResponse)
def update_research(
    research_id: int,
    research: ResearchUpdateRequest,
    db: Session = Depends(get_db),
    user: UserModel = Depends(access_only_user),
):
    check_reserach_exists(db, research_id)
    check_user_validate_by_researchID(db, research_id, user)
    db_research = ResearchRepository.get_by_id(db, research_id)
    new_research = ResearchRepository.update(db, db_research, research)
    if research.category_ids:
        new_research.category_ids = CategoryRepository.get_by_research_id(db, research_id)
    return ResearchResponse.model_validate(new_research.__dict__)


@router.delete("/{research_id}", response_model=ResearchResponse)
def delete_research(
    research_id: int, db: Session = Depends(get_db), 
    user: UserModel = Depends(only_authorized_user)
):
    check_reserach_exists(db, research_id)
    check_user_validate_by_researchID(db, research_id, user)
    research = ResearchRepository.delete(db, research_id)
    return ResearchResponse.model_validate(research.__dict__)
