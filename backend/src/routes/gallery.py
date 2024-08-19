from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse, Response

from src.database import DB
from src.utils.auth import auth_user

gallery_router = APIRouter(
    prefix='/api',
    tags=['Gallery']
)


def parse_galleries_response(galleries):
    return JSONResponse(content=[{
        'id': gallerie[0],
        'name': gallerie[1]
    } for gallerie in galleries])


@gallery_router.get('/gallery/{username:str}/{gallery:int}')
async def get_gallery_photos(username: str, gallery: int, authorization: str = Header(...)):
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
            COALESCE(GROUP_CONCAT(g.id SEPARATOR ', '), '') AS galerias
        FROM foto f
        JOIN usuario u ON f.id_usuario = u.id
        LEFT JOIN 
            (SELECT id_foto, AVG(puntaje) AS promedio_puntaje
                FROM calificacion
                GROUP BY id_foto
            ) c ON c.id_foto = f.id
        LEFT JOIN 
            (SELECT id_foto, puntaje AS puntaje_usuario
                FROM calificacion
                WHERE id_usuario = %s
            ) uc ON uc.id_foto = f.id
        LEFT JOIN 
            (SELECT id_foto
                FROM foto_favorita
                WHERE id_usuario = %s
            ) uf ON uf.id_foto = f.id
        JOIN foto_galeria fg ON fg.id_foto = f.id
        JOIN galeria g ON g.id = fg.id_galeria
        WHERE g.id = %s
        GROUP BY 
            f.id, 
            u.nombre_usuario, 
            u.nombre, 
            f.ruta_archivo, 
            f.instante_subida, 
            f.titulo, 
            f.descripcion, 
            c.promedio_puntaje, 
            uc.puntaje_usuario, 
            uf.id_foto
        ORDER BY f.instante_subida DESC;
        """,
        (auth[0], auth[0], gallery)
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
        } for photo in photos
    ])


@gallery_router.get('/gallery/{username:str}')
async def get_galleries(username: str, authorization: str = Header(...)):
    auth = auth_user(authorization)

    if isinstance(auth, Response):
        return auth

    galleries = DB.select(
        "SELECT g.id, g.nombre_galeria FROM galeria g JOIN usuario u ON g.id_usuario = u.id "
        "WHERE u.nombre_usuario = %s;",
        (username,)
    )

    return parse_galleries_response(galleries)


@gallery_router.post('/gallery/{name:str}')
async def create_gallery(name: str, authorization: str = Header(...)):
    auth = auth_user(authorization)

    if isinstance(auth, Response):
        return auth

    DB.execute(
        "INSERT INTO galeria (id_usuario, nombre_galeria) "
        "VALUES (%s, %s);",
        (auth[0], name)
    )

    galleries = DB.select(
        "SELECT g.id, nombre_galeria FROM galeria g JOIN usuario u "
        "WHERE g.id_usuario = u.id AND u.id = %s;",
        (auth[0],)
    )

    return parse_galleries_response(galleries)
