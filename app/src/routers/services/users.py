from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from ...models.user import User
from ..schemas.users import UserModel, SignupSchema
from ..repositories.users import UsersRepository
from ...dependencies import get_db


# Encrypt password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def user_signup_validate(user: SignupSchema, db: Session = Depends(get_db)):
    if UsersRepository.get_by_email(db, user.email):
        raise HTTPException(
            status_code=400, detail="User by that email already registered"
        )
    if UsersRepository.get_by_phone(db, user.phone_number):
        raise HTTPException(
            status_code=400, detail="User by that phone number already registered"
        )
    return user


def user_login_validate(user: UserModel, db: Session = Depends(get_db)):
    existing_user = UsersRepository.get_by_email(db, user.email)
    if not existing_user:
        raise HTTPException(status_code=400, detail="User not found")
        
    if not pwd_context.verify(user.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    return True