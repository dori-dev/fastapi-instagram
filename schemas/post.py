from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel

from schemas.auth import UserAuth
from schemas.comment import CommentDisplay


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str


class Post(PostBase):
    ...


class PostDisplay(PostBase):
    id: int
    timestamp: datetime
    slug: str
    user: Optional[UserAuth]
    comments: List[CommentDisplay]

    class Config:
        orm_mode = True
