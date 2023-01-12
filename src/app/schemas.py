from pydantic import BaseModel


class TodoBaseSchema(BaseModel):
    text: str
    completed: bool

    class Config:
        orm_mode = True


class TodoResponseSchema(TodoBaseSchema):
    id: int


class TodoRequestSchema(TodoBaseSchema):
    id: int
