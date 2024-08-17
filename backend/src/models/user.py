import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    birthday: datetime.date
    address: str


class UserLogin(BaseModel):
    username: str
    password: str
