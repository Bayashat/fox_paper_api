from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...dependencies import get_db, only_authorized_user
from ..schemas.comments import CommentResponse, CommentCreateRequest
from ..schemas.users import UserModel
from ..repositories.comments import CommentsRepository

router = APIRouter()

@router.get("/{research_id}/comments", response_model=List[CommentResponse])
def get_comments(
    research_id: int,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    user: UserModel = Depends(only_authorized_user)
):
    comments = CommentsRepository.get_comments(db, research_id, limit, offset)
    return [CommentResponse.model_validate(comment.__dict__) for comment in comments]


@router.post("/{research_id}/comments", response_model=CommentResponse)
def create_comment(
    research_id: int,
    comment: CommentCreateRequest,
    db: Session = Depends(get_db),
    user: UserModel = Depends(only_authorized_user)
):
    comment = CommentsRepository.create_comment(db, research_id, comment, user.id)
    return CommentResponse.model_validate(comment.__dict__)


@router.get("/{research_id}/comments/{comment_id}", response_model=CommentResponse)
def get_comment(
    research_id: int,
    comment_id: int,
    db: Session = Depends(get_db),
    user: UserModel = Depends(only_authorized_user)
):
    comment = CommentsRepository.get_comment(db, research_id, comment_id)
    return CommentResponse.model_validate(comment.__dict__)

@router.delete("/{research_id}/comments/{comment_id}")
def delete_comment(
    research_id: int,
    comment_id: int,
    db: Session = Depends(get_db),
    user: UserModel = Depends(only_authorized_user)
):
    db_comment = CommentsRepository.get_comment(db, research_id, comment_id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    CommentsRepository.delete_comment(db, research_id, comment_id)
    
    return {"message": "Comment deleted successfully"}