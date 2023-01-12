# pull official base image
FROM python:3.11-slim


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION 1.2.1
ENV POETRY_HOME /opt/poetry
ENV POETRY_NO_INTERACTION 1
ENV PATH $POETRY_HOME/bin:$PATH

RUN apt-get update
RUN apt-get install --no-install-recommends -y curl build-essential
# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN pip install "poetry==$POETRY_VERSION"

ENV POETRY_VIRTUALENVS_IN_PROJECT 1

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app
