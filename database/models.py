from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database.db import base


class UserModel(base):
    __tablename__ = 'users'

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String(50), index=True)
    email = Column(String(100))
    password = Column(String(50))
    articles = relationship('ArticleModel', backref='author')


class ArticleModel(base):
    __tablename__ = 'articles'

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String(500))
    content = Column(String)
    slug = Column(String(8))
    published_at = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
