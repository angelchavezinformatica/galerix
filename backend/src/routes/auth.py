from fastapi import APIRouter
from fastapi.responses import Response

from src.database import DB
from src.models.user import UserCreate

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@auth_router.post('/create')
async def create_user(user: UserCreate):
    data = DB.select(
        f"SELECT id FROM usuario WHERE nombre_usuario='{user.username}';",
        many=False
    )

    if data is not None:
        return Response(status_code=409)

    DB.execute(
        f"""INSERT INTO usuario (nombre_usuario, contrasena, nombre, fecha_nacimiento, direccion)
            VALUES ('{user.username}', '{user.password}', '{user.name}',
                    '{user.birthday}', '{user.address}');"""
    )

    return Response()
