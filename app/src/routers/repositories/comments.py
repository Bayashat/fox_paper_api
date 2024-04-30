from sqlalchemy.orm import Session

from app.src.models.comment import Comment
from app.src.routers.schemas.comments import CommentCreateRequest
from app.src.routers.services.db import add_commit_refresh, delete_commit

class CommentsRepository:
    @staticmethod
    def get_comments(db: Session, research_id: int, offset: int, limit: int):
        return db.query(Comment).filter(Comment.research_id == research_id).limit(limit).offset(offset).all()
    
    @staticmethod
    def create_comment(db: Session, research_id: int, comment: CommentCreateRequest, user_id: int):
        db_comment = Comment(
            content=comment.content,
            research_id=research_id,
            user_id=user_id
        )
        add_commit_refresh(db, db_comment)
        return db_comment
    
    @staticmethod
    def delete_comment(db: Session, research_id: int, comment_id: int):
        db_comment = db.query(Comment).filter(Comment.research_id == research_id, Comment.id == comment_id).first()
        delete_commit(db, db_comment)
        return db_comment