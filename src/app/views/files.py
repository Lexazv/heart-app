from fastapi import APIRouter, Request, status

from src.app.db_handlers.files import store_file_to_db, store_heart_data
from src.app.schemas.requests import FileRequest
from src.app.schemas.responses import FileData
from src.services.auth import token_required
from src.services.heart.files import get_file_details

files = APIRouter()


@files.post(
    '/', response_model=FileData, status_code=status.HTTP_201_CREATED
)
@token_required
async def create_heart_data_file(request: Request, file_data: FileRequest):
    with request.app.db.begin() as conn:
        stored_file = await store_file_to_db(
            conn=conn, file=file_data, user_id=request.state.current_user.id
        )
        heart_data = get_file_details(filename=file_data.filename)

        store_heart_data(conn=conn, data=heart_data, file=stored_file['id'])

    return stored_file
