from time import sleep
from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from schemas.user import Article, ArticleDisplay, ArticleDetail, BaseUser
from db import article as article_db
from db.database import get_db
from auth.oauth2 import get_current_user

router = APIRouter(prefix='/article', tags=['article'])


async def sample_time_suspend():
    sleep(5)
    return True


@router.get('/', response_model=List[ArticleDisplay])
async def get_all_articles(db=Depends(get_db)):
    await sample_time_suspend()
    return article_db.get_articles(db)


@router.post(
    '/',
    response_model=ArticleDisplay,
    status_code=status.HTTP_201_CREATED
)
def create_article(
        article: Article,
        db=Depends(get_db),
        current_user: BaseUser = Depends(get_current_user)
):
    print(current_user)
    print(current_user.username)
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
