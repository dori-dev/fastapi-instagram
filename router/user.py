from fastapi import APIRouter, Depends

from schemas import User, UserDisplay
from database.user import insert_user
from database.db import get_db

router = APIRouter(prefix='/user', tags=['user'])


@router.post('/', response_model=UserDisplay)
def create_user(user: User, db=Depends(get_db)):
    return insert_user(db, user)
