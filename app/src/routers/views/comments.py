from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from typing import List

from app.src.dependencies import get_db, only_authorized_user
from app.src.routers.repositories.comments import CommentsRepository
from app.src.routers.schemas.comments import CommentResponse, CommentCreateRequest
from app.src.routers.schemas.users import UserModel
from app.src.routers.services.researches import check_reserach_exists
from app.src.routers.services.users import check_user_validate_by_userID
from app.src.routers.services.comment import check_comment_exists

router = APIRouter(prefix="/researches", tags=["comments"])

@router.get("/{research_id}/comments", response_model=List[CommentResponse])
def get_comments(
    research_id: int,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    user: UserModel = Depends(only_authorized_user)
):
    check_reserach_exists(db, research_id)
    comments = CommentsRepository.get_comments(db, research_id, offset, limit)
    return [CommentResponse.model_validate(comment.__dict__) for comment in comments]


@router.post("/{research_id}/comments", response_model=CommentResponse)
def create_comment(
    research_id: int,
    comment: CommentCreateRequest,
    db: Session = Depends(get_db),
    user: UserModel = Depends(only_authorized_user)
):
    check_reserach_exists(db, research_id)
    comment = CommentsRepository.create_comment(db, research_id, comment, user.id)
    return CommentResponse.model_validate(comment.__dict__)


@router.delete("/{research_id}/comments/{comment_id}", response_model=CommentResponse)
def delete_comment(
    research_id: int,
    comment_id: int,
    db: Session = Depends(get_db),
    user: UserModel = Depends(only_authorized_user)
):
    check_reserach_exists(db, research_id)
    check_comment_exists(db, research_id, comment_id)
    comment_author_id = CommentsRepository.get_user_id_by_comment_id(db, comment_id)
    check_user_validate_by_userID(db, comment_author_id, user)
    comment = CommentsRepository.delete_comment(db, research_id, comment_id)
    
    return CommentResponse.model_validate(comment.__dict__)