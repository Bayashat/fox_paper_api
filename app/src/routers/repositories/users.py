from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from passlib.context import CryptContext
from ..schemas.users import SignupSchema, UserUpdate
from app.src.models.user import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UsersRepository:
    @staticmethod
    def create_user(db: Session, user: SignupSchema):
        hashed_password = pwd_context.hash(user.password)
        new_user = User(
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email,
            phone_number = user.phone_number,
            password = hashed_password,
            gender = user.gender,
            date_of_birth = user.date_of_birth,
            biography = user.biography,
            role_id = 1
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    
    
    @staticmethod
    def get_by_email(db:Session, email: str):
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_by_id(db:Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_by_phone(db:Session, phone_number: str):
        return db.query(User).filter(User.phone_number == phone_number).first()
    
    @staticmethod
    def update(db: Session, db_user: User, user: UserUpdate):
        for key,value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)
        
        db.commit()
        db.refresh(db_user)
        
        return db_user

    @staticmethod
    def delete(db: Session, db_user: User):
        db.delete(db_user)
        db.commit()

        return db_user