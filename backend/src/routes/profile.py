from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse, Response

from src.database import DB
from src.models.user import UserTextUpdate
from src.utils.auth import auth_user

profile_router = APIRouter(
    prefix='/api',
    tags=['Profile']
)


def get_response_profile(authorization: str = None, username: str = None):
    auth = auth_user(authorization, is_token_data=True)

    if isinstance(auth, Response):
        return auth

    _auth, token_data = auth

    user = DB.select(
        "SELECT id, nombre_usuario, nombre, fecha_nacimiento, direccion "
        "FROM usuario WHERE nombre_usuario=%s;",
        (token_data.get('username') if username is None else username,),
        many=False
    )

    emails = DB.select(
        "SELECT correo FROM correo_usuario WHERE id_usuario=%s;",
        (user[0],)
    )

    galleries = DB.select(
        "SELECT g.id, nombre_galeria FROM galeria g JOIN usuario u ON g.id_usuario = u.id "
        "WHERE u.nombre_usuario = %s;",
        (token_data.get('username') if username is None else username,)
    )

    page = DB.select(
        "SELECT p.id FROM pagina p JOIN usuario u ON p.id_usuario = u.id "
        "WHERE u.id=%s;",
        (_auth[0],),
        many=False
    )

    photos = DB.select(
        "SELECT COUNT(*) FROM foto WHERE id_usuario=%s;",
        (user[0],),
        many=False
    )

    text = DB.select(
        "SELECT contenido FROM pagina_principal WHERE id_usuario=%s;",
        (user[0],),
        many=False
    )

    return JSONResponse(content={
        'username': user[1],
        'name': user[2],
        'birthday': str(user[3]),
        'address': user[4],
        'emails': [row[0] for row in emails],
        'galleries': [{
            'id': gallerie[0],
            'name': gallerie[1]
        } for gallerie in galleries],
        'page': page is not None,
        'numphotos': photos[0],
        'text': text[0] if text is not None else '',
    })


@profile_router.get('/profile')
async def get_user_profile(authorization: str = Header(...)):
    return get_response_profile(authorization)


@profile_router.get('/profile/{username:str}')
async def get_profile(username: str, authorization: str = Header(...)):
    return get_response_profile(authorization, username)


@profile_router.patch('/profile/text')
async def update_text(text: UserTextUpdate, authorization: str = Header(...)):
    auth = auth_user(authorization)

    if isinstance(auth, Response):
        return auth

    DB.execute(
        "UPDATE pagina_principal SET contenido = %s WHERE id_usuario=%s;",
        (text.text, auth[0])
    )

    return Response()


@profile_router.get('/search-user/{name:str}')
async def search_user(name: str, authorization: str = Header(...)):
    auth = auth_user(authorization)

    if isinstance(auth, Response):
        return auth

    users = DB.select(
        "SELECT nombre, nombre_usuario FROM usuario WHERE LOWER(nombre) LIKE LOWER(%s)",
        (f"%{name}%",)
    )

    return JSONResponse(content=[{'name': user[0], 'username': user[1]} for user in users])


@profile_router.post('/page')
async def create_page(authorization: str = Header(...)):
    auth = auth_user(authorization)

    if isinstance(auth, Response):
        return auth

    page_id = DB.select(
        "SELECT p.id FROM usuario u JOIN pagina p ON p.id_usuario = u.id "
        "WHERE u.id = %s;",
        (auth[0],),
        many=False
    )

    if page_id is not None:
        return Response(status_code=409)

    DB.execute(
        "INSERT INTO pagina (id_usuario) VALUES (%s);",
        (auth[0],)
    )

    return Response()
