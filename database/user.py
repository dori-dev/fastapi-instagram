from sqlalchemy.orm.session import Session
from schemas import User
from database.models import UserModel
from database.hash import Hash


def insert_user(db: Session, request: User):
    user = UserModel(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
