from pydantic import Field
from pydantic_settings import BaseSettings
from functools import lru_cache

class ENV(BaseSettings):
    MONGO_URL: str = Field(..., description="MongoDB URL is required")
    DATABASE_NAME: str = Field(..., description="MongoDB Database Name is required")
    SECRET_KEY: str = Field(..., description="Secret Key is required")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    class Config:
        env_file = ".env"


@lru_cache
def get_env():
    return ENV()

env = get_env()