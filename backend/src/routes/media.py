import os

from fastapi import APIRouter
from fastapi.responses import FileResponse

media_router = APIRouter(
    prefix='/media',
    tags=['Media']
)


@media_router.get('/{filename:str}')
def get_photo(filename: str):
    path = os.path.join(os.getcwd(), 'media', filename)

    return FileResponse(path)
