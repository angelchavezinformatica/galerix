from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response

from src.database import DB
from src.models.user import UserCreate, UserLogin
from src.utils.auth import create_token, get_hash, verify_hash

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@auth_router.post('/create')
async def create_user(user: UserCreate):
    data = DB.select(
        f"SELECT id FROM usuario WHERE nombre_usuario=%s;",
        (user.username,),
        many=False
    )

    if data is not None:
        return Response(status_code=409)

    hashed_password = get_hash(user.password)

    DB.execute(
        """INSERT INTO usuario (nombre_usuario, contrasena, nombre, fecha_nacimiento, direccion)
            VALUES (%s, %s, %s, %s, %s);""",
        (user.username, hashed_password, user.name, user.birthday, user.address)
    )

    if not user.emails:
        return Response()

    data = DB.select(
        f"SELECT id FROM usuario WHERE nombre_usuario=%s;",
        (user.username,),
        many=False
    )

    sql = "INSERT INTO correo_usuario (id_usuario, correo) VALUES "
    params = []

    for email in user.emails:
        if email != user.emails[0]:
            sql += ', '
        sql += f"({data[0]}, %s)"
        params.append(email)

    DB.execute(sql, params)

    return Response()


@auth_router.post('/login')
async def login(user: UserLogin):
    data = DB.select(
        "SELECT contrasena FROM usuario WHERE nombre_usuario=%s;",
        (user.username,),
        many=False
    )

    if data is None:
        return Response(status_code=404)

    if not verify_hash(user.password, data[0]):
        return Response(status_code=400)

    token = create_token(data={'username': user.username})

    return JSONResponse(content={'token': token})
