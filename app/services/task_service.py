from app.db.database import task_collection
from fastapi import HTTPException
from app.models.user import UserResponse
from app.models.task import TaskCreate, TaskInDB, TaskUpdate
from app.utils.status_codes import BAD_REQUEST, NOT_FOUND

async def create_task_service(current_user: UserResponse ,task: TaskCreate):
    print(current_user)
    print(task)
    pass

async def get_task_service(current_user: UserResponse, task_id: str):
    pass

async def update_task_service(current_user: UserResponse, task_id: str, task: TaskUpdate):
    pass

async def delete_task_service(current_user: UserResponse, task_id: str):
    pass

async def get_all_task_service(current_user: UserResponse):
    pass

async def delete_all_task_service(current_user: UserResponse):
    pass
