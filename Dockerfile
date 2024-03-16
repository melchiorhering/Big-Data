# Single stage
FROM --platform=linux/amd64 python:3.10-slim-bullseye

WORKDIR /workspaces/Big-Data

# Install Java and other dependencies
RUN apt-get update && apt-get -y install git curl default-jdk procps --fix-missing && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
# ENV JAVA_HOME=/usr/lib/jvm/default-java

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi --no-root

# Install ipykernel and create a new kernel
RUN poetry run python -m ipykernel install --name=big-data

COPY entrypoint.sh ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

# # Keep the container running - this is a common pattern for Devcontainers
# CMD tail -f /dev/null
