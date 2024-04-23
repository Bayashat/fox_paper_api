from fastapi import HTTPException
from sqlalchemy.orm import Session

from ...models.research import Research, ResearchCategories
from ...models.id_abc import Status
from ...models.file import File
from ..schemas.researches import ResearchCreateRequest, ResearchUpdateRequest
from ..repositories.categories import CategoryRepository

class ResearchRepository:
    @staticmethod
    def get_researches(db: Session, limit: int, offset: int, search_text: str = None, category_ids: str = None, status: Status = None):
        query = db.query(Research)
        if status:
            query = query.filter(Research.status == status)
        
        query = query.filter(Research.status == Status.PUBLISHED)
        if search_text:
            query = query.filter(Research.title.ilike(f"%{search_text}%") | Research.description.ilike(f"%{search_text}%"))

        if category_ids:
            categories = [int(id) for id in category_ids.split(',')]
            query = query.join(ResearchCategories).filter(ResearchCategories.category_id.in_(categories))   

        researches = query.limit(limit).offset(offset).all()
        return researches
    
    
    @staticmethod
    def create_research(db: Session, research: ResearchCreateRequest, user_id: int):
        db_research = Research(
            title=research.title,
            description=research.description,
            file_id=research.file_id,
            status=Status.SUBMITTED,
            author_id=user_id
        )
        db.add(db_research)
        db.commit()
        db.refresh(db_research)
        
        categories = [int(id) for id in research.category_ids.split(',')]
        
        for category_id in categories:
            db_category = ResearchCategories(
                research_id=db_research.id,
                category_id=category_id
            )
            db.add(db_category)
        
        db.commit()
        db.refresh(db_research)
        
        # return research with categories
        db_research.category_ids = categories
        return db_research
    
    @staticmethod
    def get_by_id(db: Session, research_id: int):
        # should be also published
        return db.query(Research).filter(Research.id == research_id, Research.status == Status.PUBLISHED).first()
        
    
    @staticmethod
    def update(db: Session, db_research: Research, research: ResearchUpdateRequest):
        # first, check category ids
        if research.category_ids:
            categories = [int(id) for id in research.category_ids.split(',')]
            for category_id in categories:
                if not CategoryRepository.get_by_id(db, category_id):
                    raise HTTPException(status_code=404, detail=f"Category with id {category_id} not found")
                # first delete previous categories
                db.query(ResearchCategories).filter(ResearchCategories.research_id == db_research.id).delete()
                
                # then, add the categories to the research
                db_category = ResearchCategories(
                    research_id=db_research.id,
                    category_id=category_id
                )
                db.add(db_category)  
            db.commit()
            db.refresh(db_research)
              
        for key, value in research.model_dump(exclude_unset=True).items():
            if key == 'category_ids':
                continue
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

    
    @staticmethod
    def get_under_review(db: Session):
        return db.query(Research).filter(Research.status == Status.UNDER_REVIEW).all()

    @staticmethod
    def get_rejected(db: Session):
        return db.query(Research).filter(Research.status == Status.REJECTED).all()