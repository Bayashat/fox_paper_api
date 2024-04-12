from typing import Callable, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.src.dependencies import get_db, JWTBearer
from app.src.routers.repositories.users import UsersRepository
from ..schemas.users import UserResponse, UserUpdate



router = APIRouter()


@router.get("/", response_model=List[UserResponse])
def get_users(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    users = UsersRepository.get_users(db, skip=skip, limit=limit)
    return [UserResponse.model_validate(user.__dict__) for user in users]

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    auth: Callable = Depends(JWTBearer())
):
    user = UsersRepository.get_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse.model_validate(user.__dict__)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    auth: Callable = Depends(JWTBearer())
):
    db_user = UsersRepository.get_by_id(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    new_user = UsersRepository.update(db, db_user, user)
    return UserResponse.model_validate(new_user.__dict__)


@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    auth: Callable = Depends(JWTBearer())
):
    db_user = UsersRepository.get_by_id(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return UsersRepository.delete(db, db_user)