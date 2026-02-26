from typing import List

from app.db.database import task_collection
from fastapi import HTTPException, status
from app.models.user import UserResponse
from app.models.task import TaskCreate, TaskInDB, TaskUpdate, TaskResponse


async def create_task_service(current_user: UserResponse ,task: TaskCreate):
    task_db = TaskInDB(title=task.title, user_id=current_user.id)
    await task_collection().insert_one(task_db.model_dump(by_alias=True))
    return task_db

async def get_task_service(current_user: UserResponse, task_id: str):
    pass

async def update_task_service(current_user: UserResponse, task_id: str, task: TaskUpdate):
    pass

async def delete_task_service(current_user: UserResponse, task_id: str):
    pass

async def get_all_task_service(current_user: UserResponse):
    return await task_collection().find({}).to_list(length=None)

async def delete_all_task_service(current_user: UserResponse):
    pass
