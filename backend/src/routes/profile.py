from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse, Response

from src.database import DB
from src.utils.auth import auth_user, decode_token

profile_router = APIRouter(
    prefix='/api',
    tags=['Profile']
)


def get_response_profile(authorization: str, username: str = None):
    try:
        token = authorization.split('Bearer ')[1]
        token_data = decode_token(token)
    except Exception:
        return Response(status_code=401)

    user = DB.select(
        "SELECT id, nombre_usuario, nombre, fecha_nacimiento, direccion"
        "FROM usuario WHERE nombre_usuario=%s;",
        (token_data.get('username') if username is None else username,),
        many=False
    )

    emails = DB.select(
        "SELECT correo FROM correo_usuario WHERE id_usuario=%s;",
        (user[0],)
    )

    return JSONResponse(content={
        'username': user[1],
        'name': user[2],
        'birthday': str(user[3]),
        'address': user[4],
        'emails': [row[0] for row in emails]
    })


@profile_router.get('/profile')
async def get_profile(authorization: str = Header(...)):
    return get_response_profile(authorization)


@profile_router.get('/profile/{username:str}')
async def get_profile(username: str, authorization: str = Header(...)):
    return get_response_profile(authorization, username)


@profile_router.get('/search-user/{name:str}')
async def search_user(name: str, authorization: str = Header(...)):
    auth = auth_user(authorization)

    if auth is not None:
        return auth

    users = DB.select(
        "SELECT nombre, nombre_usuario FROM usuario WHERE LOWER(nombre) LIKE LOWER(%s)",
        (f"%{name}%",)
    )

    return JSONResponse(content=[{'name': user[0], 'username': user[1]} for user in users])
