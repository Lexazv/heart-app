from typing import List
from datetime import datetime

from pydantic import BaseModel


class UserProfile(BaseModel):

    id: int
    email: str
    first_name: str
    last_name: str
    heart_data: List[str] = []


class UserCreated(BaseModel):

    id: int
    email: str
    created_on: datetime


class Token(BaseModel):

    token: str


class FileCreated(BaseModel):

    id: int
    user: int
    filename: str
    created_on: datetime


class UserFiles(BaseModel):

    files: list = []
