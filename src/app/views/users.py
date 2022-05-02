from fastapi import APIRouter, HTTPException, Request, status

from src.app.db_handlers.files import get_files_by_user_id
from src.app.db_handlers.users import (
    check_user_by_email, context, create_user, get_user_by_email
)
from src.app.schemas.requests import UserData, UserLogin
from src.app.schemas.responses import UserCreated
from src.services.auth import create_access_token, token_required

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


@users.post('/login')
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

    return {"token": token}


@users.get('/{user_id}/files')
@token_required
async def get_user_files(user_id: int, request: Request):
    with request.app.db.begin() as conn:
        if request.state.current_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND
            )
        user_files = get_files_by_user_id(conn=conn, user_id=user_id)

    return user_files
