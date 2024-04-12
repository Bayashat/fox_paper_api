from sqlalchemy.orm import Session
from ...models.comment import Comment
from ..schemas.comments import CommentCreateRequest

class CommentsRepository:
    
    @staticmethod
    def get_comments(db: Session, research_id: int, limit: int, offset: int):
        return db.query(Comment).filter(Comment.research_id == research_id).limit(limit).offset(offset).all()
    
    @staticmethod
    def create_comment(db: Session, research_id: int, comment: CommentCreateRequest, user_id: int):
        db_comment = Comment(
            content=comment.content,
            research_id=research_id,
            user_id=user_id
        )
        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)
        return db_comment
    
    @staticmethod
    def get_comment(db: Session, research_id: int, comment_id: int):
        return db.query(Comment).filter(Comment.research_id == research_id, Comment.id == comment_id).first()
    
    @staticmethod
    def delete_comment(db: Session, research_id: int, comment_id: int):
        db_comment = db.query(Comment).filter(Comment.research_id == research_id, Comment.id == comment_id).first()
        db.delete(db_comment)
        db.commit()
        return db_comment