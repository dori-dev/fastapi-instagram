from sqlalchemy.orm.session import Session
from schemas import User
from database.models import UserModel
from database.hash import Hash


def create_user(db: Session, request: User):
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
