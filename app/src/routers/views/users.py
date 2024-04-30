from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from typing import Callable, List

from app.src.dependencies import get_db, access_only_user, only_authorized_user
from app.src.routers.repositories.users import UsersRepository
from app.src.routers.schemas.users import UserModel, UserUpdate
from app.src.routers.services.users import check_user_validate_by_userID


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserModel])
def get_users(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    users = UsersRepository.get_users(db, skip=skip, limit=limit)
    return [UserModel.model_validate(user.__dict__) for user in users]

@router.get("/{user_id}", response_model=UserModel)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    auth: Callable = Depends(access_only_user)
):
    user = UsersRepository.get_by_id(db, user_id)
    return UserModel.model_validate(user.__dict__)


@router.patch("/{user_id}", response_model=UserModel)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    auth: Callable = Depends(only_authorized_user)
):
    db_user = UsersRepository.get_by_id(db, user_id)
    new_user = UsersRepository.update(db, db_user, user)
    return UserModel.model_validate(new_user.__dict__)


@router.delete("/{user_id}", response_model=UserModel)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    auth: Callable = Depends(access_only_user)
):
    check_user_validate_by_userID(db, user_id, auth)
    db_user = UsersRepository.delete(db, user_id)
    return UserModel.model_validate(db_user.__dict__)