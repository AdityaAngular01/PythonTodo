from fastapi import APIRouter, Depends

from app.core.dependencies import get_current_user
from app.models.user import UserCreate, UserLogin, UserResponse
from app.controllers.auth_controller import signup_controller, login_controller

router = APIRouter(prefix="/auth", tags=["auth", "Auth Routes"])

@router.post("/signup")
async def signup(user: UserCreate):
    return await signup_controller(user)

@router.post("/login")
async def login(user: UserLogin):
    return await login_controller(user)

@router.get("/profile", response_model=UserResponse)
async def get_profile(current_user: UserResponse = Depends(get_current_user)):
    return current_user