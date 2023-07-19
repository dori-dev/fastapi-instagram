from pydantic import BaseModel


class UserAuth(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
