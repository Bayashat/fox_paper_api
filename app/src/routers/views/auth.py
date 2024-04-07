from fastapi import APIRouter, Form, Depends, status
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.src.dependencies import get_db
from app.src.dependencies import create_jwt, decode_jwt
from app.src.routers.repositories.users import UsersRepository
from app.src.routers.schemas.users import CreateUser
from fastapi import HTTPException


router = APIRouter()

# 1. Registration
@router.post("/users")
def register_user(
    user: CreateUser,
    db: Session = Depends(get_db)
):
    new_user = UsersRepository.create_user(db, user)
    
    return new_user


# 2. Login
@router.post("/users/login")
def login_user(
    email: EmailStr = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = UsersRepository.get_by_email(db, email)
    
    if user.password != password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    token = create_jwt(user.id)
    return {"access_token": token, "token_type": "bearer"}