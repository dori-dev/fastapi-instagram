from string import ascii_letters
from random import choices
import datetime

from sqlalchemy.orm.session import Session
from schemas.user import Article
from db.models import ArticleModel


def generate_slug(db: Session, length=8):
    slug = "".join(choices(ascii_letters, k=length))
    while db.query(ArticleModel).filter(ArticleModel.slug == slug).first():
        slug = "".join(choices(ascii_letters, k=length))
    return slug


def create_article(db: Session, request: Article):
    now = datetime.datetime.now()
    slug = generate_slug(db)
    article = ArticleModel(
        title=request.title,
        content=request.content,
        user_id=request.author_id,
        published=request.published,
        published_at=now,
        slug=slug,
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_articles(db: Session):
    return db.query(ArticleModel).all()


def get_article(db: Session, slug):
    try:
        return db.query(ArticleModel).filter(ArticleModel.slug == slug).first()
    except Exception:
        return None
