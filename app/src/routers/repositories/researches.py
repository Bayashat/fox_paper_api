from fastapi import HTTPException
from sqlalchemy.orm import Session
from ...models.research import Research, ResearchCategories
from ..schemas.researches import ResearchCreateRequest
from ...models.id_abc import Status
from ..repositories.categories import CategoryRepository

class ResearchRepository:
    @staticmethod
    def get_researches(db: Session, limit: int, offset: int):
        return db.query(Research).limit(limit).offset(offset).all()
    
    @staticmethod
    def create_research(db: Session, research: ResearchCreateRequest, user_id: int):
        db_research = Research(
            title=research.title,
            description=research.description,
            file_id=research.file_id,
            status=Status.DRAFT,
            is_published=False,
            author_id=user_id
        )
        db.add(db_research)
        db.commit()
        db.refresh(db_research)

        
        categories = research.category_ids.split(',')
        
                
        # firstly, check if the categories exist
        for category_id in categories:
            if not CategoryRepository.get_by_id(db, category_id):
                raise HTTPException(status_code=404, detail=f"Category with id {category_id} not found")
            
        # then, add the categories to the research
        for category_id in categories:
            db_category = ResearchCategories(
                research_id=db_research.id,
                category_id=category_id
            )
            db.add(db_category)
        
        db.commit()
        db.refresh(db_research)
        
        # return research with categories
        db_research.category_ids = research.category_ids
        return db_research
    
    @staticmethod
    def get_by_id(db: Session, research_id: int):
        return db.query(Research).filter(Research.id == research_id).first()
        
    
    @staticmethod
    def update(db: Session, db_research: Research, research: ResearchCreateRequest):
        for key, value in research.model_dump(exclude_unset=True).items():
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
    
    @staticmethod
    def get_by_file_id(db: Session, file_id: int):
        return db.query(Research).filter(Research.file_id == file_id).first()
