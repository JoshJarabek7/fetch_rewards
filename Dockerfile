FROM python:3.13-slim

ENV POETRY_VERSION=1.8.4

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

RUN poetry run pytest

EXPOSE 8001

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
