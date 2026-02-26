from app.models.token_response import TokenResponse
from app.services.auth_service import signup_service as user_signup, login_service as user_login
from app.models.user import UserCreate, UserLogin

async def signup_controller(user: UserCreate) -> TokenResponse:
    return await user_signup(user)

async def login_controller(user: UserLogin) -> TokenResponse:
    return await user_login(user)