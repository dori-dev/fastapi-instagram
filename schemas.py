from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str
    email: str


class User(BaseUser):
    password: str


class UserDisplay(BaseUser):
    id: int

    class Config:
        orm_mode = True
