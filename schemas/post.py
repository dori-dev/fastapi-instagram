from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    username: str

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    user: User


class Post(PostBase):
    ...


class PostDisplay(PostBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
