from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    username: str
    id: int

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str


class Post(PostBase):
    user_id: int


class PostDisplay(PostBase):
    id: int
    timestamp: datetime
    slug: str
    user: Optional[User]

    class Config:
        orm_mode = True
