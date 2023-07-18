import re
from sqlalchemy.orm.session import Session

from schemas import User
from db.models import UserModel
from db.hash import Hash
from exceptions import EmailNotValid


def check_email(email):
    pattern = r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-]+)(\.[a-zA-Z]{2,5}){1,2}$"
    if not re.match(pattern, email):
        raise EmailNotValid('Email is not valid!')


def create_user(db: Session, request: User):
    check_email(request.email)
    user = UserModel(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(UserModel).all()


def get_user(db: Session, id):
    try:
        return db.query(UserModel).filter(UserModel.id == id).first()
    except Exception:
        return None


def get_user_by_username(db: Session, username):
    try:
        return db.query(UserModel).filter(UserModel.username == username).first()
    except Exception:
        return None


def delete_user(db: Session, id):
    user = get_user(db, id)
    if user is None:
        return False
    db.delete(user)
    db.commit()
    return True


def update_user(db: Session, id, request: User):
    user = db.query(UserModel).filter(UserModel.id == id)
    user.update({
        "username": request.username,
        "email": request.email,
        "password": Hash.bcrypt(request.username),
    })
    db.commit()
    return request
