from fastapi import HTTPException

from app.src.models.favorite import Favorite


def check_favorite_exists(db, user_id: int, favorite_id: int):
    favorite = db.query(Favorite).filter(
        Favorite.user_id == user_id, Favorite.id == favorite_id
    ).first()
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found.")


def check_favorite_not_exists(db, user_id: int, research_id: int):
    favorite = db.query(Favorite).filter(
        Favorite.user_id == user_id, Favorite.research_id == research_id
    ).first()
    if favorite:
        raise HTTPException(status_code=400, detail="Favorite already exists.")