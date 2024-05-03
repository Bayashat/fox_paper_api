from app.src.models.category import Category
from app.src.models.category import ResearchCategories

from sqlalchemy.orm import Session


class CategoryRepository:
    @staticmethod
    def get_by_research_id(db: Session, research_id: int) -> list[dict]:
        results = db.query(Category.id, Category.name)\
                    .join(ResearchCategories, ResearchCategories.category_id == Category.id)\
                    .filter(ResearchCategories.research_id == research_id)\
                    .all()
        return [{"id": id, "name": name} for id, name in results]


    @staticmethod
    def get_by_id(db: Session, category_id: int) -> Category:
        return db.query(Category).filter(Category.id == category_id).first()
