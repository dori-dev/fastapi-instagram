from sqlalchemy import (
    Column, ForeignKey,
    Integer, String, DateTime,
)
from sqlalchemy.orm import relationship

from db.database import base


class UserModel(base):
    __tablename__ = 'users'

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String(50), index=True)
    email = Column(String(100))
    password = Column(String(50))
    posts = relationship('PostModel', back_populates='user')


class PostModel(base):
    __tablename__ = 'posts'

    id = Column(Integer, index=True, primary_key=True)
    slug = Column(String(8), index=True)
    image_url = Column(String(1024))
    image_url_type = Column(String(100))
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('UserModel', back_populates='posts')
