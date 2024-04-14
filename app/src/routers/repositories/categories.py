from ...models.category import Category
from ...models.research import ResearchCategories

from sqlalchemy.orm import Session

class CategoryRepository:
    @staticmethod
    def get_by_research_id(db: Session, research_id):
        # only return the categories's ids
        research_categories: Category = db.query(ResearchCategories).filter(ResearchCategories.research_id == research_id).all()
        return ','.join([str(research_category.category_id) for research_category in research_categories])
        
        
    
    @staticmethod
    def get_by_id(db: Session, category_id: int) -> Category:
        return db.query(Category).filter(Category.id == category_id).first()