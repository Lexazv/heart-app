from fastapi import APIRouter

from src.app.views import users, files


router = APIRouter()


router.include_router(users.users, prefix='/users', tags=['users'])
router.include_router(files.files, prefix='/files', tags=['files'])
