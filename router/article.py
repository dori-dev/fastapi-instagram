from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from schemas import Article, ArticleDisplay, ArticleDetail, Author
from database import article as article_db
from database.db import get_db

router = APIRouter(prefix='/article', tags=['article'])


@router.get('/', response_model=List[ArticleDisplay])
def get_all_articles(db=Depends(get_db)):
    return article_db.get_articles(db)


@router.post(
    '/',
    response_model=ArticleDisplay,
    status_code=status.HTTP_201_CREATED
)
def create_article(article: Article, db=Depends(get_db)):
    return article_db.create_article(db, article)


@router.get('/{slug}', response_model=ArticleDetail)
def get_article_detail(slug: str, db=Depends(get_db)):
    article = article_db.get_article(db, slug)
    if article:
        return article
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Article "{slug}" not found!',
    )
