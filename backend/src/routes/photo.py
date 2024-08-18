import base64
import datetime
import os
from uuid import uuid4

from fastapi import APIRouter, Header
from fastapi.responses import Response

from src.database import DB
from src.models.photo import UploadPhoto
from src.utils.auth import auth_user

photo_router = APIRouter(
    prefix='/api',
    tags=['Photo']
)


@photo_router.post('/photo')
def upload_photo(photo: UploadPhoto, authorization: str = Header(...)):
    auth = auth_user(authorization)

    if isinstance(auth, Response):
        return auth

    image_data = photo.image.split(',')[1]
    image_bytes = base64.b64decode(image_data)
    filename = f'{uuid4()}.{photo.file_extension}'
    path = os.path.join(os.getcwd(), 'media', filename)

    last_id = DB.execute(
        "INSERT INTO foto (id_usuario, ruta_archivo, instante_subida, titulo, descripcion) "
        "VALUES (%s, %s, %s, %s, %s);",
        (auth[0], filename, datetime.datetime.now(),
         photo.title, photo.description)
    )

    with open(path, mode='wb') as f:
        f.write(image_bytes)

    if not len(photo.gallery_ids):
        return Response()

    sql = "INSERT INTO foto_galeria VALUES "

    for gid in photo.gallery_ids:
        if gid != photo.gallery_ids[0]:
            sql += ', '
        sql += f'({gid}, {last_id})'

    DB.execute(sql)

    return Response()
