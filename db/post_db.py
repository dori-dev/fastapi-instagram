import datetime
from string import ascii_letters
from random import choices
from sqlalchemy.orm.session import Session

from schemas.post import Post
from db.models import PostModel


def generate_slug(db: Session, length=8):
    slug = "".join(choices(ascii_letters, k=length))
    while db.query(PostModel).filter(PostModel.slug == slug).first():
        slug = "".join(choices(ascii_letters, k=length))
    return slug


def create_post(db: Session, request: Post):
    post = PostModel(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        user_id=request.user_id,
        slug=generate_slug(db),
        timestamp=datetime.datetime.now(),
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_all_posts(db: Session):
    return db.query(PostModel).all()
