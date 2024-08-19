import datetime

from pydantic import BaseModel
from typing import List


class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    birthday: datetime.date
    address: str
    emails: List[str]


class UserLogin(BaseModel):
    username: str
    password: str


class UserTextUpdate(BaseModel):
    text: str
