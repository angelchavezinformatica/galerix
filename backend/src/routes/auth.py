from datetime import timedelta

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

    token = create_token(data={'username': user.username},
                         expires_delta=timedelta(days=1))

    return JSONResponse(content={'token': token})
