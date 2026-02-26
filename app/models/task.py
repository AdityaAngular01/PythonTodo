from pydantic import BaseModel, Field
from app.utils.helper import PyObjectId
from bson import ObjectId


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)

class TaskInDB(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    is_completed: bool = False
    user_id: PyObjectId

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class TaskResponse(BaseModel):
    title: str
    is_completed: bool