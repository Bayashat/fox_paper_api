from sqlalchemy.orm import Session
from ...models.user import Research

class ResearchRepository:
    @staticmethod
    def get_researches(db: Session, limit: int, offset: int):
        return db.query(Research).limit(limit).offset(offset).all()