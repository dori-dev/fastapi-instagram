from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from schemas import User, UserDisplay
from database import user as user_db
from database.db import get_db

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/', response_model=List[UserDisplay])
def get_all_users(db=Depends(get_db)):
    return user_db.get_users(db)


@router.post(
    '/',
    response_model=UserDisplay,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: User, db=Depends(get_db)):
    return user_db.create_user(db, user)


@router.get('/{id}', response_model=UserDisplay)
def get_user_detail(id: int, db=Depends(get_db)):
    user = user_db.get_user(db, id)
    if user:
        return UserDisplay.from_orm(user)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Use with id {id} not found!',
    )


@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db=Depends(get_db)):
    if user_db.delete_user(db, id):
        return {}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Use with id {id} not found!',
    )


@router.put('/update/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update_user(id: int, user: User, db=Depends(get_db)):
    return user_db.update_user(db, id, user)
