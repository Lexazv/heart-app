from fastapi import APIRouter, HTTPException, Request, status

from src.app.db_handlers.users import (
    create_user, get_user_by_email, check_user_by_email, context
)
from src.services.auth import create_access_token, token_required
from src.app.schemas.requests import UserData, UserLogin
from src.app.schemas.responses import UserProfile, UserCreated, Token


users = APIRouter()

@users.get('/hello')
async def welcome():
    return {'message': 'Hello! This is a service for heart disease prediction!'}


@users.post(
    '/registration', 
    response_model=UserCreated, 
    status_code=status.HTTP_201_CREATED
)
async def registration(request: Request, user_data: UserData):
    with request.app.db.begin() as conn:
        existing_user = check_user_by_email(email=user_data.email, conn=conn)

        if existing_user:
            raise HTTPException(
                status_code=400, detail='user with entered email already exists'
            )
        user = create_user(conn=conn, user_data=user_data)

    return user


@users.post('/login', response_model=Token)
async def login_user(request: Request, user_data: UserLogin):
    with request.app.db.begin() as conn:
        request_user = get_user_by_email(conn=conn, email=user_data.email)

        if not (
            request_user and context.verify(
                user_data.password, request_user.password
            )
        ):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        token = create_access_token(email=user_data.email)

    return token


@users.get('/{user_id}', response_model=UserProfile)
@token_required
async def get_user_profile(user_id: int, request: Request):
    current_user = request.state.current_user

    if current_user.id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)              # Update to get heart data + nested schemas response

    return current_user
