from datetime import datetime, timedelta, timezone

import bcrypt
import jwt

from config import CONFIG


def verify_hash(plain: str, hashed: str):
    return bcrypt.checkpw(plain.encode('utf-8'), hashed.encode('utf-8'))


def get_hash(plain: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain.encode('utf-8'), salt)


def create_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,
                             CONFIG.get('SECRET_KEY'),
                             algorithm=CONFIG.get('ALGORITHM'))
    return encoded_jwt
