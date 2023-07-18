from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from schemas.post import Post, PostDisplay
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
def create_post(post: Post, db: Session = Depends(get_db)):
    if post.image_url_type not in IMAGE_URL_TYPES:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Image url type must be 'url' or 'uploaded'.",
        )
    return post_db.create_post(db, post)


@router.get('/', response_model=List[PostDisplay])
def get_posts(db: Session = Depends(get_db)):
    return post_db.get_all_posts(db)
