from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.app.schemas import TodoBaseSchema, TodoResponseSchema, TodoRequestSchema
import src.app.crud as crud
from src.app.db import get_db


todo_router = APIRouter()


@todo_router.get("", response_model=list[TodoResponseSchema])
def read_todos(db: Session = Depends(get_db)) -> list[TodoResponseSchema]:
    todos = crud.read_todos(db)
    return todos


@todo_router.post("", response_model=TodoResponseSchema)
def add_todo(
        todo_data: TodoBaseSchema,
        db: Session = Depends(get_db)
) -> TodoResponseSchema:
    todo = crud.add_todo(db, todo_data)
    return todo


@todo_router.put("", response_model=TodoResponseSchema)
def update_todo(
        todo_data: TodoRequestSchema,
        db: Session = Depends(get_db)
) -> TodoResponseSchema:
    todo = crud.update_todo(db, todo_data)
    return todo


@todo_router.delete("/{todo_id}")
def delete_todo(
        todo_id: int,
        db: Session = Depends(get_db)
) -> dict:
    deleted = crud.delete_todo(db, todo_id)
    return {"deleted": deleted}
