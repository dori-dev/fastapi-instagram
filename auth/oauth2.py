from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from sqlalchemy.orm import Session

from database.db import get_db
from database.user import get_user_by_username


SECRET_KEY = "44406a8683a220cc7ec77b4d967b70149cfe527a6ba017295aa72278fdf212b3"
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db),
):
    error_credential = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid credentials',
        headers={
            'WWW-authenticate': 'bearer',
        },
    )
    try:
        dict_ = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = dict_.get('sub')
        if username is None:
            raise error_credential
    except JWTError:
        raise error_credential
    user = get_user_by_username(db, username)
    return user
