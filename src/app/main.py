from fastapi import FastAPI
from src.app.routers.todos import todo_router
from . import models
from .db import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo Service",
    description="A simple todo service",
    version="0.1.0",
    docs_url="/",
)

app.include_router(todo_router, prefix="/api")



