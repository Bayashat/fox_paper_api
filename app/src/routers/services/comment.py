from fastapi import HTTPException

from app.src.models.comment import Comment


def check_comment_exists(db, research_id: int, comment_id: int):
    if not db.query(Comment).filter(Comment.research_id == research_id, Comment.id == comment_id).first():
        raise HTTPException(status_code=404, detail="Comment not found")
    