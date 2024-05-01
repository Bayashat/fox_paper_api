from fastapi import HTTPException

from sqlalchemy.orm import Session

from passlib.context import CryptContext

from app.src.models.user import User
from app.src.routers.schemas.users import SignupSchema, UserUpdate
from app.src.routers.services.users import check_user_not_exists, hash_and_save_user, check_role_id
from app.src.routers.services.db import delete_commit


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
    def get_by_id(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    @staticmethod
    def get_by_email(db: Session, email: str):
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def update(db: Session, db_user: User, user: UserUpdate):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
        check_role_id(user.role_id)
        
        update_data = user.model_dump(exclude_unset=True, exclude={"password"})
            
        for key, value in update_data.items():
            setattr(db_user, key, value)
        
        if user.password:
            db_user.password = pwd_context.hash(user.password)
            
        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def delete(db: Session, user_id: int):
        db_user = UsersRepository.get_by_id(db, user_id)
        delete_commit(db, db_user)
        return db_user
