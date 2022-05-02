from datetime import datetime

from pydantic import BaseModel


class UserCreated(BaseModel):

    id: int
    email: str
    created_on: datetime


class FileData(BaseModel):

    id: int
    user: int
    filename: str
    extention: str
    created_on: datetime
