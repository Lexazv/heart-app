from unittest.mock import ANY

from src.app.config import settings

VALID_USER_DATA = {
    "email": "testemail@gmail.com",
    "password": "Password1234567",
    "confirmed_password": "Password1234567",
    "first_name": "Test",
    "last_name": "User",
}


USER_PROFILE = {
    "email": "testemail@gmail.com",
    "first_name": "Test",
    "last_name": "User",
    "heart_data": [],
}


INVALID_ERROR_RESPONSE = {
    "detail": [{"loc": [ANY, ANY], "msg": ANY, "type": ANY}]
}

TOKEN_RESPONSE = {"token": ANY}


TOKEN_PAYLOAD = {"email": ANY, "exp": ANY}


PAYLOAD_ENCODE_ARGS = [
    ({"email": "testemail@gmail.com", "exp": ANY}, ANY),
    {"algorithm": settings.ALGORITHM},
]

PAYLOAD_DECODE_ARGS = [(ANY), {"algorithms": "HS512"}]
