FROM python:3.11-slim-bullseye

WORKDIR /app

RUN pip install uv
COPY ./src/pyproject.toml ./src/uv.lock /app/
ENV UV_PROJECT_ENVIRONMENT=/root/.venv \
    UV_CACHE_DIR=/root/.cache
RUN uv sync

COPY ./src /app/
VOLUME /static/

COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
