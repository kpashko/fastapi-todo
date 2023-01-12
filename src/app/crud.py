from typing import List

from .models import TodoModel
from .schemas import TodoBaseSchema, TodoResponseSchema, TodoRequestSchema

from sqlalchemy.orm import Session


def read_todos(
        db: Session,
) -> List[TodoModel]:
    """
    Read all todos from the database.

    Args:
        db (Session): The database session.

    Returns:
        List[TodoModel]: A list of TodoModel objects.
    """
    todos = db.query(TodoModel).all()

    return todos


def add_todo(
        db: Session,
        todo_data: TodoBaseSchema,
) -> TodoModel:
    """
    Add a todo item to the database.

    Args:
        db (Session): The database session.
        todo_data (TodoBaseSchema): The todo data.

    Returns:
        TodoModel: The TodoModel object.
    """
    todo: TodoModel = TodoModel(
        text=todo_data.text,
        completed=todo_data.completed,
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


def update_todo(
        db: Session,
        new_todo: TodoRequestSchema,
) -> TodoModel:
    """
    Update a todo item in the database.

    Args:
        db (Session): The database session.
        new_todo (TodoRequestSchema): The new todo data.

    Returns:
        TodoModel: The TodoModel object.
    """
    todo: TodoModel = db.query(TodoModel).filter(
        TodoModel.id == new_todo.id,
    ).first()

    todo.text = new_todo.text
    todo.completed = new_todo.completed

    db.commit()
    db.refresh(todo)

    return todo


def delete_todo(
        db: Session,
        todo_id: int,
) -> bool:
    """
    Delete a todo item from the database.

    Args:
        db (Session): The database session.
        todo_id (int): The todo id.

    Returns:
        bool: The return value. True if the record was deleted, False otherwise.
    """
    deleted: int = db.query(TodoModel).filter(TodoModel.id == todo_id).delete()

    db.commit()

    return deleted > 0

