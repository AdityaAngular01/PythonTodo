from app.db.database import user_collection
from app.core.security import hash_password, verify_password, access_token_generator
from fastapi import HTTPException

from app.models.user import UserCreate, UserInDB
from app.utils.status_codes import BAD_REQUEST


async def signup_service(user: UserCreate):
    existing_user = await user_collection().find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=BAD_REQUEST, detail="User already exists")

    hashed_password = hash_password(user.password)

    user_db = UserInDB( full_name=user.full_name, email=user.email, hashed_password=hashed_password)

    await user_collection().insert_one(user_db.model_dump(by_alias=True))
    token = access_token_generator({"sub": str(user_db.id)})
    return {"access_token": token, "token_type": "bearer"}


async def login_service(user):
    db_user = await user_collection().find_one({"email": user.email})
    if not db_user:
        raise HTTPException(status_code=BAD_REQUEST, detail="Invalid credentials")

    if not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=BAD_REQUEST, detail="Invalid credentials")

    token = access_token_generator({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}