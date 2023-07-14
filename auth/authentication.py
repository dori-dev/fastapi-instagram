from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from database import models
from database.db import get_db
from database.hash import Hash
from auth import oauth2


router = APIRouter(tags=['auth'])


@router.post('/token')
def get_token(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(models.UserModel).filter(
        models.UserModel.username == request.username
    ).first()
    if user is None or Hash.verify(request.password, user.password) is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Invalid username or password.',
        )
    access_token = oauth2.create_access_token(data={'sub': user.username})
    return {
        'access_token': access_token,
        'type_token': 'bearer',
        'userId': user.id,
        'username': user.username,
    }
