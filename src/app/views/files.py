from fastapi import APIRouter, Request, status, HTTPException

from src.app.schemas.requests import FileRequest
from src.app.schemas.responses import FileCreated, UserFiles
from src.services.auth import token_required
from src.services.heart.files import get_file_details
from src.app.db_handlers.files import (
    store_heart_data, store_file_to_db, get_files_by_user_id
)


files = APIRouter()


@files.post(
    '/', response_model=FileCreated, status_code=status.HTTP_201_CREATED
)
@token_required
async def create_heart_data_file(request: Request, file_data: FileRequest):
    with request.app.db.begin() as conn:
        stored_file = store_file_to_db(
            conn=conn, file=file_data, user_id=request.state.current_user.id
        )
        heart_data = get_file_details(filename=file_data.filename)

        store_heart_data(conn=conn, data=heart_data, file=stored_file['id'])

    return stored_file


@files.get('/{user_id}', response_model=UserFiles)
@token_required
async def get_user_files(user_id: int, request: Request):
    with request.app.db.begin() as conn:
        if request.state.current_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND
            )
        user_files = get_files_by_user_id(conn=conn, user_id=user_id)

    return user_files
