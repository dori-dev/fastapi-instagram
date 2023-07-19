from datetime import datetime

from pydantic import BaseModel

from schemas.auth import UserAuth


class CommentBase(BaseModel):
    text: str
    timestamp: datetime


class Comment(CommentBase):
    user_id: int
    post_id: int


class CommentDisplay(CommentBase):
    id: int
    user: UserAuth

    class Config:
        orm_mode = True
