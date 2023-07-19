from datetime import datetime

from pydantic import BaseModel

from schemas.auth import UserAuth


class CommentBase(BaseModel):
    text: str


class Comment(CommentBase):
    user_id: int
    post_id: int


class CommentDisplay(CommentBase):
    id: int
    user: UserAuth
    timestamp: datetime

    class Config:
        orm_mode = True
