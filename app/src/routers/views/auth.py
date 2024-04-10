from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.src.dependencies import (
    get_db,
    only_authorized_user,
    access_only_admin,
    access_only_researcher,
    access_only_standard_user,
)
from app.src.routers.repositories.users import UsersRepository
from ..schemas.users import SignupSchema, LoginSchema, ProfileSchema, UserModel
from app.src.dependencies import JWTRepo


router = APIRouter()

# Encrypt password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: SignupSchema, db: Session = Depends(get_db)):
    existing_user = UsersRepository.get_by_email(db, user.email)
    if existing_user:
        raise HTTPException(
            status_code=400, detail="User by that email already registered"
        )

    if UsersRepository.get_by_phone(db, user.phone_number):
        raise HTTPException(
            status_code=400, detail="User by that phone number already registered"
        )
    UsersRepository.create_user(db, user)
    return {"message": user}


@router.post("/login", status_code=status.HTTP_200_OK)
def user_login(request: LoginSchema, db: Session = Depends(get_db)):
    existing_user = UsersRepository.get_by_email(db, request.email)
    if existing_user is None:
        raise HTTPException(status_code=400, detail="User not found")

    if not pwd_context.verify(request.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    token = JWTRepo.generate_token({"sub": request.email})
    return {"access_token": token, "token_type": "Bearer"}


@router.get("/profile", response_model=ProfileSchema, status_code=status.HTTP_200_OK)
def user_profile(user: UserModel = Depends(only_authorized_user)):
    return ProfileSchema(**dict(user))
