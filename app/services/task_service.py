from typing import List

from app.db.database import task_collection
from fastapi import HTTPException, status
from app.models.user import UserResponse
from app.models.task import TaskCreate, TaskInDB, TaskUpdate, TaskResponse
from bson import ObjectId



async def create_task_service(current_user: UserResponse ,task: TaskCreate):
    task_db = TaskInDB(title=task.title, user_id=current_user.id)
    await task_collection().insert_one(task_db.model_dump(by_alias=True))
    return task_db

async def get_task_service(current_user: UserResponse, task_id: str)-> TaskResponse:
    task = await task_collection().find_one({"_id": ObjectId(task_id), "user_id": ObjectId(current_user.id)})
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return TaskResponse(**task)

async def update_task_service(current_user: UserResponse, task_id: str, task: TaskUpdate) -> TaskResponse:
    update_result = await task_collection().update_one({"_id": ObjectId(task_id), "user_id": ObjectId(current_user.id)}, {
        "$set": {
            "title": task.title,
            "is_completed": task.is_completed,
        }
    })
    if update_result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return await get_task_service(current_user, task_id)

async def delete_task_service(current_user: UserResponse, task_id: str):
    delete_result = await task_collection().delete_one({"_id": ObjectId(task_id), "user_id": ObjectId(current_user.id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"message": "Task deleted successfully"}

async def get_all_task_service(current_user: UserResponse):
    tasks = await task_collection().find(
        {"user_id": current_user.id}
    ).to_list(length=None)

    return [
        TaskResponse(
            **{**task, "_id": str(task["_id"])}
        )
        for task in tasks
    ]

async def delete_all_task_service(current_user: UserResponse):
    delete_result = await task_collection().delete_many({"user_id": ObjectId(current_user.id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No tasks found")
    return {"message": "All tasks deleted successfully"}
