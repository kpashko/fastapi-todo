from sqlalchemy import Boolean, Column, Integer, Text
from .db import Base


class TodoModel(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    completed = Column(Boolean, default=False)
