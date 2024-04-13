from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.src.dependencies import (
    get_db,
    only_authorized_user,
    access_only_moderator,
    access_only_researcher,
    access_only_standard_user,
)
from app.src.routers.repositories.users import UsersRepository
from ..schemas.users import SignupSchema, LoginSchema, ProfileSchema, UserModel
from app.src.dependencies import JWTRepo
from ..services.users import user_signup_validate, user_login_validate

router = APIRouter()


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: SignupSchema, db: Session = Depends(get_db)):
    if user_signup_validate(db=db, user=user):
        new_user = UsersRepository.create_user(db, user)
        token = JWTRepo.generate_token({"sub": new_user.email})
        return {
            "access_token": token,
            "user": UserModel.model_validate(new_user.__dict__),
        }


@router.post("/login", status_code=status.HTTP_200_OK)
def user_login(request: LoginSchema, db: Session = Depends(get_db)):
    if user_login_validate(db=db, user=request):
        token = JWTRepo.generate_token({"sub": request.email})
        return {
            "access_token": token,
            "user": UserModel.model_validate(
                UsersRepository.get_by_email(db, request.email).__dict__
            ),
        }


# @router.get("/profile", response_model=ProfileSchema, status_code=status.HTTP_200_OK)
# def user_profile(user: UserModel = Depends(only_authorized_user)):
#     return ProfileSchema(**dict(user))
