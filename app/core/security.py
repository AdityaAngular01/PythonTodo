from passlib.context import CryptContext
from datetime import datetime, timedelta
from app.core.config import env as ENV
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hashing a password
def hash_password(password: str)->str:
    return pwd_context.hash(password)

# Verifying a password
def verify_password(plain_password: str, hashed_password: str)->bool:
    return pwd_context.verify(plain_password, hashed_password)

# Access Token
def access_token_generator(data: dict)->str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes= ENV.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, ENV.SECRET_KEY, algorithm=ENV.ALGORITHM)