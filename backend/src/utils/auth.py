import bcrypt
import jwt

from fastapi.responses import Response

from config import CONFIG
from src.database import DB


def verify_hash(plain: str, hashed: str):
    return bcrypt.checkpw(plain.encode('utf-8'), hashed.encode('utf-8'))


def get_hash(plain: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain.encode('utf-8'), salt)


def create_token(data: dict):
    return jwt.encode(data.copy(),
                      CONFIG.get('SECRET_KEY'),
                      algorithm=CONFIG.get('ALGORITHM'))


def decode_token(token: str):
    return jwt.decode(token, CONFIG.get('SECRET_KEY'),
                      algorithms=[CONFIG.get('ALGORITHM')])


def auth_user(authorization: str, is_token_data: bool = False):
    try:
        token = authorization.split('Bearer ')[1]
        token_data = decode_token(token)
    except Exception:
        return Response(status_code=401)

    user = DB.select(
        "SELECT id FROM usuario WHERE nombre_usuario=%s;",
        (token_data.get('username'),),
        many=False
    )

    if user is None:
        return Response(status_code=401)

    if is_token_data:
        return user, token_data

    return user
