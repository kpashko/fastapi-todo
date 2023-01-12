from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.app.db import Base, get_db
from src.app.main import app

import copy

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

todo_blob = {"id": 1, "text": "test_todo", "completed": False}


def test_add_todo():
    payload = copy.copy(todo_blob)
    payload.pop("id")

    response = client.post(
        "/api",
        json=payload
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    assert data["text"] == payload["text"]
    assert data["completed"] == payload["completed"]


def test_read_todos():
    response = client.get("/api")
    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data) > 0


def test_update_todo():
    payload = copy.copy(todo_blob)
    payload["text"] = "updated_todo"
    payload["completed"] = True
    import pprint
    pprint.pp(vars(client.get("/api")))
    response = client.put("/api", json=payload)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == payload["id"]
    assert data["text"] == payload["text"]
    assert data["completed"] == payload["completed"]


def test_delete_todos():
    payload = todo_blob
    response = client.delete(f"/api/{payload['id']}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["deleted"] is True


def test_delete_todo_404():
    response = client.delete("/api/999")
    assert response.status_code == 404, response.text
