from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from typing import List

from app.src.dependencies import get_db, access_only_user
from app.src.routers.repositories.favorite import FavoriteRepository
from app.src.routers.schemas.users import UserModel
from app.src.routers.schemas.favorite import FavoriteSchema
from app.src.routers.services.researches import check_reserach_exists
from app.src.routers.services.favorite import check_favorite_exists, check_favorite_not_exists

router = APIRouter(prefix="/favorites", tags=["favorites"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_favorite(
    research_id: int, 
    db: Session = Depends(get_db), 
    user: UserModel = Depends(access_only_user)
):
    check_reserach_exists(db, research_id)
    check_favorite_not_exists(db, user.id, research_id)
    FavoriteRepository.add_favorite(db, user.id, research_id)
    return {"message": "Research added to favorites successfully."}


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_favorite(
    id: int, 
    db: Session = Depends(get_db), 
    user: UserModel = Depends(access_only_user)
):
    check_favorite_exists(db, user.id, id)
    FavoriteRepository.delete_favorite(db, user.id, id)
    return {"message": "Research removed from favorites successfully."}


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[FavoriteSchema])
def get_favorites(
    db: Session = Depends(get_db), 
    user: UserModel = Depends(access_only_user)
):
    favorites = FavoriteRepository.list_favorites(db, user.id)
    return favorites