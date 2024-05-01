from fastapi.security import  HTTPBearer
from fastapi import Depends, Request, HTTPException, status, UploadFile, File

from jose import jwt
import os

from app.src.database import SessionLocal
from .routers.repositories.users import UsersRepository
from .routers.schemas.users import UserModel
from .config import settings


# Database part
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class JWTRepo:
    @staticmethod
    def generate_token(data: dict):
        return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    @staticmethod
    def decode_token(token: str):
        try:
            return jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        except Exception as e:
            print(f"Error decoding token: {e}")
            return None


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authendication scheme"
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token"
                )
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")

    def verify_jwt(self, jwt_token: str) -> bool:
        is_token_valid: bool = False

        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        except:
            payload = None

        if payload:
            is_token_valid = True
        return is_token_valid


def get_token_data(token: str = Depends(JWTBearer())):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = JWTRepo.decode_token(token)
    if token_data is None:
        raise credentials_exception
    return token_data


def access_only_moderator(token_data: dict = Depends(get_token_data), db=Depends(get_db)):
    user_email = token_data["sub"]
    existing_user = UsersRepository.get_by_email(db=db, email=user_email)

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User not found",
        )

    if existing_user.role_id != 2:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not a Moderator",
        )

    return existing_user


def access_only_user(
    token_data: dict = Depends(get_token_data), db=Depends(get_db)
):
    user_email = token_data["sub"]
    existing_user = UsersRepository.get_by_email(db=db, email=user_email)

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User not authorized",
        )

    if existing_user.role_id != 1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not a researcher",
        )

    return existing_user


def only_authorized_user(
    token_data: dict = Depends(get_token_data), db=Depends(get_db)
):
    user_email = token_data["sub"]
    existing_user = UsersRepository.get_by_email(db=db, email=user_email)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User not authorized",
        )
    return UserModel.model_validate(existing_user.__dict__)

async def validate_file_size(file: UploadFile = File(...)):  
    max_size = 10 * 1024 * 1024  # 10 MB limit
    file.file.seek(0, os.SEEK_END)  # move the cursor to the end of the file
    file_size = file.file.tell()  # get size of the file
    if file_size > max_size:
        raise HTTPException(status_code=413, detail="File too large")
    file.file.seek(0)
    return file