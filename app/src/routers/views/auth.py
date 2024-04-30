from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.src.dependencies import get_db, JWTRepo
from app.src.routers.repositories.users import UsersRepository
from app.src.routers.schemas.auth import AuthResponse
from app.src.routers.schemas.users import SignupSchema, LoginSchema, UserModel
from app.src.routers.services.users import user_login_validate

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=AuthResponse)
def signup(user: SignupSchema, db: Session = Depends(get_db)):
    new_user = UsersRepository.create_user(db, user)
    token = JWTRepo.generate_token({"sub": new_user.email})
    return AuthResponse.model_validate(
        {
            "access_token": token,
            "user": UserModel.model_validate(new_user.__dict__),
        }
    )


@router.post("/login", status_code=status.HTTP_200_OK, response_model=AuthResponse)
def user_login(request: LoginSchema, db: Session = Depends(get_db)):
    user_login_validate(db, request)
    token = JWTRepo.generate_token({"sub": request.email})
    return AuthResponse.model_validate(
        {
            "access_token": token,
            "user": UserModel.model_validate(
                UsersRepository.get_by_email(db, request.email).__dict__
            ),
        }
    )
