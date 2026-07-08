from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.core.dbconnection import (SECRET_KEY,ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES )


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def pass_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def create_access_token(data: dict):
    payload = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({"exp":expire})

    token = jwt.encode(
        payload,
        SECRET_KEY,
        ALGORITHM
    )
    return token