from sqlalchemy import Column, Integer, String
from database.db import base


class UserModel(base):
    __tablename__ = 'users'
    id = Column(Integer, index=True, primary_key=True)
    username = Column(String(63), index=True)
    email = Column(String(127))
    password = Column(String(63))
