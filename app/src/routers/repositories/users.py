from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..schemas.users import SignupSchema, UserUpdate
from ...models.user import User
from app.src.routers.services.users import check_user_not_exists, hash_and_save_user


class UsersRepository:
    @staticmethod
    def create_user(db: Session, user: SignupSchema):
        check_user_not_exists(db, user)
        new_user = hash_and_save_user(db, user)
        return new_user
    
    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 20):
        users = db.query(User).offset(skip).limit(limit).all()
        return users


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
        if user.password:
            db_user.password = pwd_context.hash(user.password)
        
        if user.role_id and user.role_id not in [1, 2] or user.role_id == 0:
            raise HTTPException(status_code=400, detail="Invalid role_id")
            
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