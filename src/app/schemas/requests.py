import os
import re

from pydantic import BaseModel, validator, root_validator

from src.constants import FileExtentions, PASSWORD_TEMPLATE, EMAIL_TEMPLATE


# Users requests.
class UserData(BaseModel):

    email: str
    password: str
    confirmed_password: str
    first_name: str
    last_name: str

    @validator('email')
    def validate_email(cls, email: str) -> str:
        template = re.compile(EMAIL_TEMPLATE)

        if not template.match(email):
            raise ValueError('invalid email')

        return email

    @root_validator
    def validate_passwords(cls, values: dict) -> dict:
        template = re.compile(PASSWORD_TEMPLATE)

        if values.get('password') != values.get('confirmed_password'):
            raise ValueError('passwords are not equal')

        elif not template.match(values.get('password')):
            raise ValueError('insecure password')

        values.pop('confirmed_password')

        return values

    @root_validator
    def validate_personal_data(cls, values: dict) -> dict:
        if not all(
            data.isalpha() and len(data) > 2 for data in [
                values.get('first_name'), values.get('last_name')
            ]
        ):
            raise ValueError('invalid personal data')
        return values


class UserLogin(BaseModel):

    email: str
    password: str


# File requests.
class FileRequest(BaseModel):

    filename: str

    @validator('filename')
    def validate_filename(cls, filename: str):
        if os.path.splitext(filename)[-1] != FileExtentions.csv.value:
            raise ValueError('invalid file extention')
        
        return filename
