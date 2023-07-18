from typing import List

from pydantic import BaseModel
from fastapi import Body

from schemas.post import PostDisplay


class UserBase(BaseModel):
    username: str
    email: Body(
        regex=r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-]+)(\.[a-zA-Z]{2,5}){1,2}$"
    )


class User(UserBase):
    password: str


class UserDisplay(UserBase):
    id: int
    posts: List[PostDisplay]

    class Config:
        orm_mode = True
