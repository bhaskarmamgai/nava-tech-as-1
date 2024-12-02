from datetime import datetime, timedelta
from jose import jwt
from decouple import config

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = "HS256"

def create_jwt_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
