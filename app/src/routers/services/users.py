from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from ...models.user import User
from ..schemas.users import UserModel, SignupSchema
from .db import add_commit_refresh


# Encrypt password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def check_user_not_exists(db: Session, user: SignupSchema):
    # check by email and phone
    user_by_email = db.query(User).filter(User.email == user.email).first()
    if user.phone_number:
        user_by_phone = db.query(User).filter(User.phone_number == user.phone_number).first()
    else:
        user_by_phone = None
    if user_by_email or user_by_phone:
        raise HTTPException(status_code=400, detail="User already exists")
    


def hash_and_save_user(db: Session, user: SignupSchema) -> User:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(user.password)
    new_user = User(**user.model_dump(), role_id=1)
    new_user.password = hashed_password
    add_commit_refresh(db, new_user)
    return new_user


def user_login_validate( db: Session, user: UserModel):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="User not found")
        
    if not pwd_context.verify(user.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")