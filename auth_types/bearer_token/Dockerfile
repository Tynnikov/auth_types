FROM python:3.10

EXPOSE 8000

WORKDIR /app

COPY poetry.lock pyproject.toml auth_types/bearer_token/main.py ./

RUN pip install poetry \
    && poetry install

CMD poetry run python ./main.py
