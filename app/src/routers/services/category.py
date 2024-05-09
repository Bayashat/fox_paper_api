from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.src.models.category import Category

def check_category_ids_valid(db: Session, category_ids: str) -> None:
    category_id_list = [id for id in category_ids.split(",")]
    for category_id in category_id_list:
        if not category_id.isdigit():
            raise HTTPException(status_code=400, detail="Invalid category_id")
        category = db.query(Category).filter(Category.id == int(category_id))
        if not category:
            raise HTTPException(status_code=400, detail=f"Category with id {category_id} does not exist")
