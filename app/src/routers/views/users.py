from typing import Callable, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ...dependencies import get_db, access_only_user, only_authorized_user
from ..repositories.users import UsersRepository
from ..schemas.users import UserModel, UserUpdate



router = APIRouter()


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

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserModel.model_validate(user.__dict__)


@router.patch("/{user_id}", response_model=UserModel)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    auth: Callable = Depends(only_authorized_user)
):
    db_user = UsersRepository.get_by_id(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    new_user = UsersRepository.update(db, db_user, user)
    return UserModel.model_validate(new_user.__dict__)


@router.delete("/{user_id}", response_model=UserModel)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    auth: Callable = Depends(access_only_user)
):
    db_user = UsersRepository.get_by_id(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    UsersRepository.delete(db, db_user)
    return {"message": "User deleted"}