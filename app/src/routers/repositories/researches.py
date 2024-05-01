from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.src.models.research import Research, ResearchCategories
from app.src.models.enums import Status
from app.src.routers.repositories.categories import CategoryRepository
from app.src.routers.schemas.researches import ResearchCreateRequest, ResearchUpdateRequest
from app.src.routers.services.file import check_file_exists
from app.src.routers.services.researches import check_reserach_exists
from app.src.routers.services.db import add_commit_refresh, delete_commit


class ResearchRepository:
    @staticmethod
    def get_researches(db: Session, limit: int, offset: int, search_text: str = None, category_ids: str = None, status: Status = None):
        query = db.query(Research)
        if status:
            query = query.filter(Research.status == status)
        else:
            query = query.filter(Research.status == Status.PUBLISHED)
            
        if search_text:
            query = query.filter(Research.title.ilike(f"%{search_text}%") | Research.description.ilike(f"%{search_text}%"))

        if category_ids:
            category_list = [int(id) for id in category_ids.split(',')]
            query = query.join(ResearchCategories).filter(ResearchCategories.category_id.in_(category_list))   

        researches = query.limit(limit).offset(offset).all()
        return researches
    
    
    @staticmethod
    def create_research(db: Session, research_data: ResearchCreateRequest, user_id: int):
        db_research = Research(
            title=research_data.title,
            description=research_data.description,
            file_id=research_data.file_id,
            status=Status.SUBMITTED,
            author_id=user_id
        )
        add_commit_refresh(db, db_research)

        # add category ids to db
        category_id_list = [int(id) for id in research_data.category_ids.split(',')]
        
        for category_id in category_id_list:
            db_category = ResearchCategories(
                research_id=db_research.id,
                category_id=category_id
            )
            db.add(db_category)
        
        db.commit()
        db.refresh(db_research)
        
        return db_research
    
    @staticmethod
    def get_by_id(db: Session, research_id: int):
        return db.query(Research).filter(Research.id == research_id, Research.status == Status.PUBLISHED).first()
        
    
    @staticmethod
    def update(db: Session, db_research: Research, research: ResearchUpdateRequest):
        # check category ids
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
        delete_commit(db, db_research)
        return db_research

