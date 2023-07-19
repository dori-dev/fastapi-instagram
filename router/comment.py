from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from schemas.comment import Comment, CommentDisplay
from schemas.auth import UserAuth
from db import comment_db
from db.database import get_db

router = APIRouter(prefix='/comment', tags=['comment'])


@router.post(
    '/create/',
    response_model=CommentDisplay,
    status_code=status.HTTP_201_CREATED
)
def create_comment(
    comment: Comment,
    db: Session = Depends(get_db),
    user: UserAuth = Depends(get_current_user),
):
    return comment_db.create_comment(db, comment, user)


@router.get('/{post_id}', response_model=List[CommentDisplay])
def get_comments(post_id: int, db: Session = Depends(get_db)):
    return comment_db.get_post_comments(db, post_id)


@router.delete(
    '/delete/{id}',
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_comment(
    id: int,
    db: Session = Depends(get_db),
    user: UserAuth = Depends(get_current_user),
):
    if comment_db.delete_comment(db, id, user.id):
        return {}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="This comment not found.",
    )
