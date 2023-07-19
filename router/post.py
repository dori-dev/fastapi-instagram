from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from schemas.post import Post, PostDisplay
from schemas.user import UserAuth
from db import post_db
from db.database import get_db

router = APIRouter(prefix='/post', tags=['post'])

IMAGE_URL_TYPES = [
    "URL",
    "UPLOADED",
]


@router.post(
    '/create/',
    response_model=PostDisplay,
    status_code=status.HTTP_201_CREATED
)
def create_post(
    post: Post,
    db: Session = Depends(get_db),
    user: UserAuth = Depends(get_current_user),
):
    if post.image_url_type not in IMAGE_URL_TYPES:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Image url type must be 'URL' or 'UPLOADED'.",
        )
    return post_db.create_post(db, post, user)


@router.get('/', response_model=List[PostDisplay])
def get_posts(db: Session = Depends(get_db)):
    return post_db.get_all_posts(db)
