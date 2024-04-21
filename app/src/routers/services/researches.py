from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..schemas.researches import ResearchCreateRequest
from ..repositories.researches import ResearchRepository
from ..repositories.categories import CategoryRepository

def research_create_validate(db: Session, research: ResearchCreateRequest):
    file = ResearchRepository.get_by_file_id(db, research.file_id)
    if file:
        # error for such file already exists
        raise HTTPException(status_code=400, detail="File already exists")
    
    # check if category_ids:str is valid
    category_ids = research.category_ids.split(",")
    for category_id in category_ids:
        if not category_id.isdigit():
            raise HTTPException(status_code=400, detail="Invalid category_id")
        category = CategoryRepository.get_by_id(db, category_id)
        if not category:
            raise HTTPException(status_code=400, detail="Invalid category_id")
    return True
