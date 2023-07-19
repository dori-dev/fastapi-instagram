import datetime
from sqlalchemy.orm.session import Session

from schemas.comment import Comment
from schemas.auth import UserAuth
from db.models import CommentModel


def create_comment(db: Session, request: Comment, user: UserAuth):
    comment = CommentModel(
        text=request.text,
        post_id=request.post_id,
        user_id=user.id,
        timestamp=datetime.datetime.now(),
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_post_comments(db: Session, post_id: int):
    return db.query(CommentModel).filter(CommentModel.post_id == post_id).all()


def get_comment(db: Session, id):
    try:
        return db.query(CommentModel).filter(CommentModel.id == id).first()
    except Exception:
        return None


def delete_comment(db: Session, id, user_id):
    comment = get_comment(db, id)
    if comment is None:
        return False
    if comment.user_id == user_id or comment.post.user.id == user_id:
        db.delete(comment)
        db.commit()
        return True
    return False
