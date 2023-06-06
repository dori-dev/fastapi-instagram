from typing import List

from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    content: str


class Article(ArticleBase):
    author_id: int


class ArticleDisplay(ArticleBase):
    slug: str
    published_at: bool

    class Config:
        orm_mode = True


class Author(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class ArticleDetail(ArticleDisplay):
    author: Author

    class Config:
        orm_mode = True


class BaseUser(BaseModel):
    username: str
    email: str


class User(BaseUser):
    password: str


class UserDisplay(BaseUser):
    id: int
    articles: List[ArticleDisplay]

    class Config:
        orm_mode = True
