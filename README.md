### Project for a simple todo API

it uses
* Python 3.11
* FastAPI
* SQLAlchemy
* Alembic
* Poetry
* Docker

OpenAPI specification would be available at: http://localhost:8000/

### How to run
To start the API service make sure you have docker installed and run the following command:
```
docker-compose up
```
or, without docker:
```
poetry shell
poetry install
alembic upgrade head
python -m uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload```
```
### Run tests
```
poetry run pytest
```