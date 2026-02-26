from pydantic import BaseModel, Field, field_validator, model_validator, EmailStr
import re as regex
from bson import ObjectId
from app.utils.helper import PyObjectId


# request model (signup)
class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    confirm_password: str

    @field_validator("password")
    def password_checker(cls, value):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
        if not regex.match(pattern, value):
            raise ValueError(
                "Password must contain uppercase, lowercase, number and special character"
            )
        return value

    @model_validator(mode="after")
    def check_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self


# DB model (stored in database)
class UserInDB(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    full_name: str
    email: EmailStr
    hashed_password: str

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# response model (returned to client)
class UserResponse(BaseModel):
    id: PyObjectId = Field(alias="_id")
    full_name: str
    email: EmailStr

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserLogin(BaseModel):
    email: EmailStr
    password: str