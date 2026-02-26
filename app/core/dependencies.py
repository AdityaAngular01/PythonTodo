from bson import ObjectId
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.config import env as ENV
from app.db.database import user_collection
from app.models.user import UserResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme))->UserResponse:
    try:
        payload = jwt.decode(token, ENV.SECRET_KEY, algorithms=[ENV.ALGORITHM])
        email: str = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = await user_collection().find_one({"email": email})

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return UserResponse(**user)