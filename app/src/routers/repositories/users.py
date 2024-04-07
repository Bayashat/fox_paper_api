from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.src.routers.schemas.users import CreateUser
from app.src.models.user import User

class UsersRepository:
    @staticmethod
    def create_user(db: Session, user: CreateUser):
        try:
            # query for email and phone
            existing_user = db.query(User).filter(User.email == user.email or User.phone_number == user.phone_number).first()
            if existing_user:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
            
            # create user
            new_user = User(**user.model_dump())
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
    
    @staticmethod
    def get_by_email(db:Session, email: str):
        return db.query(User).filter(User.email == email).first()