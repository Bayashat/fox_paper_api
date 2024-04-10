from sqlalchemy.orm import Session
from ...models.user import User
from ..schemas.users import UserCreate, UserModel


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    user_data = db.query(User).filter(User.email == email).first()
    return UserModel.model_validate(user_data.__dict__)

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    # fake_hashed_password = user.hashed_password + "notreallyhashed"
    db_user = User(**user.model_dump())
    # db_user.hashed_password = fake_hashed_password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()

# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item