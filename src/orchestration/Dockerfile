# Build stage
FROM --platform=linux/amd64 python:3.10-slim-bullseye as builder

WORKDIR /workspaces/orchestration

# Update and upgrade the package list, install necessary packages, and clean up
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi --only main --no-root

# Runtime stage
FROM python:3.10-slim-bullseye as runtime

WORKDIR /workspaces/orchestration

ENV DAGSTER_HOME=/workspaces/orchestration/src

# Change the Python version here to match the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

ENTRYPOINT ["poetry", "run", "dagster", "dev", "-h", "0.0.0.0", "-p", "3000"]
