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


@gallery_router.get('/gallery/{username:str}')
def get_galleries(username: str, authorization: str = Header(...)):
    auth = auth_user(authorization)

    if isinstance(auth, Response):
        return auth

    galleries = DB.select(
        "SELECT g.id, nombre_galeria FROM galeria g JOIN usuario u ON g.id_usuario = u.id"
        "WHERE u.nombre_usuario = %s;",
        (username,)
    )

    return parse_galleries_response(galleries)


@gallery_router.post('/gallery/{name:str}')
def create_gallery(name: str, authorization: str = Header(...)):
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
