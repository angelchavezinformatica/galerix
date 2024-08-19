import base64
import datetime
import decimal
import os
from uuid import uuid4

from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse, Response

from src.database import DB
from src.models.photo import RatePhoto, ToogleFavorite, UploadPhoto
from src.utils.auth import auth_user

photo_router = APIRouter(
    prefix='/api',
    tags=['Photo']
)


@photo_router.post('/photo')
async def upload_photo(photo: UploadPhoto, authorization: str = Header(...)):
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


@photo_router.get('/photo/all')
async def get_all_photos(authorization: str = Header(...)):
    auth = auth_user(authorization)

    if isinstance(auth, Response):
        return auth

    photos = DB.select(
        """SELECT f.id, 
            u.nombre_usuario, 
            u.nombre, 
            f.ruta_archivo, 
            f.instante_subida, 
            f.titulo, 
            f.descripcion, 
            COALESCE(c.promedio_puntaje, 0) AS promedio_puntaje,
            COALESCE(uc.puntaje_usuario, 0) AS puntaje_usuario,
            CASE 
                WHEN uf.id_foto IS NOT NULL THEN TRUE 
                ELSE FALSE 
            END AS es_favorito,
            COALESCE(GROUP_CONCAT(g.id SEPARATOR ', '), '') AS galerias
        FROM foto f
        JOIN usuario u ON f.id_usuario = u.id
        LEFT JOIN (
            SELECT id_foto, AVG(puntaje) AS promedio_puntaje
            FROM calificacion
            GROUP BY id_foto
        ) c ON c.id_foto = f.id
        LEFT JOIN (
            SELECT id_foto, puntaje AS puntaje_usuario
            FROM calificacion
            WHERE id_usuario = %s
        ) uc ON uc.id_foto = f.id
        LEFT JOIN (
            SELECT id_foto
            FROM foto_favorita
            WHERE id_usuario = %s
        ) uf ON uf.id_foto = f.id
        LEFT JOIN foto_galeria fg ON fg.id_foto = f.id
        LEFT JOIN galeria g ON g.id = fg.id_galeria
        GROUP BY f.id, u.nombre_usuario, u.nombre, f.ruta_archivo, f.instante_subida, f.titulo, f.descripcion, c.promedio_puntaje, uc.puntaje_usuario, uf.id_foto
        ORDER BY f.instante_subida DESC;""",
        (auth[0], auth[0])
    )

    return JSONResponse(content=[
        {
            'id': photo[0],
            'username': photo[1],
            'name': photo[2],
            'path': photo[3],
            'timestamp': str(photo[4]),
            'title': photo[5],
            'description': photo[6],
            'score': float(photo[7]),
            'userscore': int(photo[8]),
            'isfavorite': bool(photo[9]),
            'galleries': [int(gallery) for gallery in photo[10].split(', ')] if photo[10] else [],
        }
        for photo in photos
    ])


@photo_router.get('/photo/user/{username:str}')
async def get_user_photos(username: str, authorization: str = Header(...)):
    auth = auth_user(authorization)

    if isinstance(auth, Response):
        return auth

    photos = DB.select(
        """SELECT 
            f.id, 
            u.nombre_usuario, 
            u.nombre, 
            f.ruta_archivo, 
            f.instante_subida, 
            f.titulo, 
            f.descripcion, 
            COALESCE(c.promedio_puntaje, 0) AS promedio_puntaje,
            COALESCE(uc.puntaje_usuario, 0) AS puntaje_usuario,
            CASE 
                WHEN uf.id_foto IS NOT NULL THEN TRUE 
                ELSE FALSE 
            END AS es_favorito,
            COALESCE(GROUP_CONCAT(g.nombre_galeria SEPARATOR ', '), '') AS galerias
        FROM foto f
        JOIN usuario u ON f.id_usuario = u.id
        LEFT JOIN 
            (SELECT id_foto, AVG(puntaje) AS promedio_puntaje
            FROM calificacion
            GROUP BY id_foto) c ON c.id_foto = f.id
        LEFT JOIN 
            (SELECT id_foto, puntaje AS puntaje_usuario
            FROM calificacion
            WHERE id_usuario = (SELECT id FROM usuario WHERE nombre_usuario = %s)) uc ON uc.id_foto = f.id
        LEFT JOIN 
            (SELECT id_foto
            FROM foto_favorita
            WHERE id_usuario = (SELECT id FROM usuario WHERE nombre_usuario = %s)) uf ON uf.id_foto = f.id
        LEFT JOIN foto_galeria fg ON fg.id_foto = f.id
        LEFT JOIN galeria g ON g.id = fg.id_galeria
        WHERE u.nombre_usuario = %s
        GROUP BY f.id, u.nombre_usuario, u.nombre, f.ruta_archivo, f.instante_subida, f.titulo, f.descripcion, c.promedio_puntaje, uc.puntaje_usuario, uf.id_foto
        ORDER BY f.instante_subida DESC;""",
        (username, username, username)
    )

    return JSONResponse(content=[
        {
            'id': photo[0],
            'username': photo[1],
            'name': photo[2],
            'path': photo[3],
            'timestamp': str(photo[4]),
            'title': photo[5],
            'description': photo[6],
            'score': float(photo[7]),
            'userscore': int(photo[8]),
            'isfavorite': bool(photo[9]),
            'galleries': photo[10].split(', ') if photo[10] else [],
        }
        for photo in photos
    ])


@photo_router.put('/photo/rate')
async def rate_photo(rate: RatePhoto, authorization: str = Header(...)):
    auth = auth_user(authorization)

    if isinstance(auth, Response):
        return auth

    rating = DB.select(
        "SELECT * FROM calificacion WHERE id_usuario=%s AND id_foto=%s;",
        (auth[0], rate.photoid),
        many=False
    )

    if rating is None:
        DB.execute(
            "INSERT INTO calificacion (id_usuario, id_foto, puntaje) "
            "VALUES (%s, %s, %s);",
            (auth[0], rate.photoid, rate.rate)
        )
    else:
        DB.execute(
            "UPDATE calificacion SET puntaje = %s WHERE id_usuario=%s AND id_foto=%s;",
            (rate.rate, auth[0], rate.photoid)
        )

    return Response()


@photo_router.put('/photo/favorite')
async def toogle_favorite(toogle: ToogleFavorite, authorization: str = Header(...)):
    auth = auth_user(authorization)

    if isinstance(auth, Response):
        return auth

    favorite = DB.select(
        "SELECT * FROM foto_favorita WHERE id_usuario=%s AND id_foto=%s;",
        (auth[0], toogle.photoid),
        many=False
    )

    if favorite is None:
        DB.execute(
            "INSERT INTO foto_favorita VALUES (%s, %s);",
            (auth[0], toogle.photoid)
        )
    else:
        DB.execute(
            "DELETE FROM foto_favorita WHERE id_usuario=%s AND id_foto=%s;",
            (auth[0], toogle.photoid)
        )
