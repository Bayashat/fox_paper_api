from sqlalchemy.orm import Session

from app.src.models.favorite import Favorite
from app.src.routers.services.db import add_commit_refresh


class FavoriteRepository:
    @staticmethod
    def add_favorite(db: Session, user_id: int, research_id: int):
       favorite = Favorite(user_id=user_id, research_id=research_id)
       add_commit_refresh(db, favorite)
       
    @staticmethod
    def delete_favorite(db: Session, user_id: int, favorite_id: int):
        favorite = db.query(Favorite).filter(
            Favorite.user_id == user_id, Favorite.id == favorite_id
        ).first()
        db.delete(favorite)
        db.commit()
    
    @staticmethod
    def list_favorites(db: Session, user_id: int):
        favorites = (
            db.query(Favorite)
            .join(Favorite.research)
            .filter(Favorite.user_id == user_id)
            .all()
        )
        return favorites    