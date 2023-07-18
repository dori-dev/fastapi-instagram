from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from db.database import base


class UserModel(base):
    __tablename__ = 'users'

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String(50), index=True)
    email = Column(String(100))
    password = Column(String(50))
    articles = relationship('ArticleModel', back_populates='author')


class ArticleModel(base):
    __tablename__ = 'articles'

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String(500))
    content = Column(String)
    slug = Column(String(8))
    published = Column(Boolean)
    published_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('UserModel', back_populates='articles')
