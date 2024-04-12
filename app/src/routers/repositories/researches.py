from sqlalchemy.orm import Session
from ...models.research import Research
from ..schemas.researches import ResearchCreateRequest
from ...models.id_abc import Status

class ResearchRepository:
    @staticmethod
    def get_researches(db: Session, limit: int, offset: int):
        return db.query(Research).limit(limit).offset(offset).all()
    
    @staticmethod
    def create_research(db: Session, research: ResearchCreateRequest):
        db_research = Research(
            title=research.title,
            description=research.description,
            file_id=research.file_id,
            status=Status.DRAFT,
            is_published=False
        )
        db.add(db_research)
        db.commit()
        db.refresh(db_research)
        return db_research
    
    @staticmethod
    def get_by_id(db: Session, research_id: int):
        return db.query(Research).filter(Research.id == research_id).first()
        
    
    @staticmethod
    def update(db: Session, db_research: Research, research: ResearchCreateRequest):
        for key,value in research.model_dump(exclude_unset=True).items():
            setattr(db_research, key, value)
        
        db.commit()
        db.refresh(db_research)
        return db_research
    
    
    @staticmethod
    def delete(db: Session, research_id: int):
        db_research = db.query(Research).filter(Research.id == research_id).first()
        db.delete(db_research)
        db.commit()
        return db_research