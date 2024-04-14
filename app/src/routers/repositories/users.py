from sqlalchemy.orm import Session
from passlib.context import CryptContext

from ..schemas.users import SignupSchema, UserUpdate, UserModel
from ...models.user import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UsersRepository:
    @staticmethod
    def create_user(db: Session, user: SignupSchema):
        hashed_password = pwd_context.hash(user.password)
        new_user = User(**user.model_dump())
        new_user.password = hashed_password
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

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