from fastapi import APIRouter, status
from fastapi.params import Depends
from app.core.dependencies import get_current_user
from app.models.task import TaskCreate, TaskUpdate
from app.models.user import UserResponse

router = APIRouter(prefix= "/task", tags= ["task", "Task Routes"],)

from app.controllers.task_controller import create_task_controller, get_all_task_controller, get_task_controller, update_task_controller, delete_task_controller, delete_all_task_controller

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate, current_user: UserResponse = Depends(get_current_user)):
    return await create_task_controller(current_user, task)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_task(current_user: UserResponse = Depends(get_current_user)):
    return await get_all_task_controller(current_user)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_task(current_user: UserResponse = Depends(get_current_user)):
    return await delete_all_task_controller(current_user)

@router.get("/{task_id}", status_code=status.HTTP_200_OK)
async def get_task(task_id: str, current_user: UserResponse = Depends(get_current_user)):
    return await get_task_controller(current_user, task_id)

@router.put("/{task_id}", status_code=status.HTTP_200_OK)
async def update_task(task_id: str, updated_task: TaskUpdate, current_user: UserResponse = Depends(get_current_user)):
    return await update_task_controller(current_user, task_id, updated_task)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: str, current_user: UserResponse = Depends(get_current_user)):
    return await delete_task_controller(current_user, task_id)
