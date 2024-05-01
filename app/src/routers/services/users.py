from fastapi import HTTPException

from sqlalchemy.orm import Session

from passlib.context import CryptContext

from app.src.models.user import User
from app.src.models.research import Research
from app.src.routers.schemas.users import UserModel, SignupSchema
from .db import add_commit_refresh


# Encrypt password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_and_save_user(db: Session, user: SignupSchema) -> User:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(user.password)
    new_user = User(**user.model_dump(), role_id=1)
    new_user.password = hashed_password
    add_commit_refresh(db, new_user)
    return new_user


def check_user_not_exists(db: Session, user: SignupSchema):
    # check by email and phone
    user_by_email = db.query(User).filter(User.email == user.email).first()
    if user.phone_number:
        user_by_phone = db.query(User).filter(User.phone_number == user.phone_number).first()
    else:
        user_by_phone = None
    if user_by_email or user_by_phone:
        raise HTTPException(status_code=400, detail="User already exists")
    
    
def user_login_validate( db: Session, user: UserModel):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="User not found")
        
    if not pwd_context.verify(user.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
def check_role_id(role_id: int):
    if role_id and role_id not in [1, 2] or role_id == 0:
        raise HTTPException(status_code=400, detail="Invalid role_id")
    
def check_user_validate_by_researchID(db: Session, research_id: int, user: UserModel):
    author_id_str = db.query(Research).filter(Research.id == research_id).first().author_id
    author_id = int(author_id_str)
    if user.role_id == 1 and user.id != author_id:
        raise HTTPException(status_code=403, detail="You are not authorized to delete this research")

def check_user_validate_by_userID(db: Session, user_id: int, user: UserModel):
    print(user_id, user.id)
    if user.role_id == 1 and user.id != user_id:
        raise HTTPException(status_code=403, detail="You are not authorized to do this action")
