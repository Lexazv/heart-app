from functools import wraps
from datetime import datetime, timedelta

from jose.jwt import decode, encode
from pytz import timezone
from fastapi import HTTPException, status

from src.app.config import settings
from src.app.db_handlers.users import get_user_by_email


def create_access_token(email: str) -> str:
    data = dict(email=email, exp=datetime.now(
        timezone('Europe/Kiev')) + timedelta(minutes=15)
    )
    token = encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return {'token': token}


def get_token_payload(token: str) -> dict:
    payload = decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
    return payload


def token_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            request = kwargs['request']
            token = request.headers['Authorization']
            payload = get_token_payload(token)

            with request.app.db.begin() as conn:
                current_user = get_user_by_email(
                    conn=conn, email=payload['email']
                )
            request.state.current_user = current_user

        except Exception as exc:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Unathorized user!'
            ) from exc

        result = await func(*args, **kwargs)
        return result
    return wrapper
