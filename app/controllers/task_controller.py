from app.models.task import TaskUpdate, TaskResponse, TaskCreate
from app.models.user import UserResponse
from app.services.task_service import (
    create_task_service as create_task,
    get_task_service as get_task_by_id,
    get_all_task_service as fetch_all_tasks,
    update_task_service as update_task,
    delete_task_service as delete_task,
    delete_all_task_service as delete_all_tasks
)
from typing import List

async def create_task_controller(current_user:UserResponse, task: TaskCreate):
    return await create_task(current_user, task)

async def get_task_controller(current_user:UserResponse, task_id: str) -> TaskResponse:
    return await get_task_by_id(current_user, task_id)

async def get_all_task_controller(current_user:UserResponse):
    return await fetch_all_tasks(current_user)

async def update_task_controller(current_user:UserResponse, task_id: str, task: TaskUpdate):
    return await update_task(current_user, task_id, task)

async def delete_task_controller(current_user:UserResponse, task_id: str):
    return await delete_task(current_user, task_id)

async def delete_all_task_controller(current_user:UserResponse):
    return await delete_all_tasks(current_user)