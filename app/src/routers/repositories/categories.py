from ...models.category import Category
from ...models.research import ResearchCategories

from sqlalchemy.orm import Session

class CategoryRepository:
    @staticmethod
    def get_by_research_id(db: Session, research_id) -> list[int]:
        # only return the categories's ids
        research_categories: ResearchCategories = db.query(ResearchCategories).filter(ResearchCategories.research_id == research_id).all()
        category_ids =  [research_category.category_id for research_category in research_categories]
        # categories = [CategoryRepository.get_by_id(db, category_id) for category_id in category_ids]
        category_names = [CategoryRepository.get_by_id(db, category_id).name for category_id in category_ids]
        # return like: [{"id": 1, "name": "category1"}, {"id": 2, "name": "category2"}]
        return [{"id": category_id, "name": category_name} for category_id, category_name in zip(category_ids, category_names)]
        
        
    
    @staticmethod
    def get_by_id(db: Session, category_id: int) -> Category:
        return db.query(Category).filter(Category.id == category_id).first()