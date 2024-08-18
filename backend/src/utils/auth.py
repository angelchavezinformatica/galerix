import bcrypt
import jwt

from config import CONFIG


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
