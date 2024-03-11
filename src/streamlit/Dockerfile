FROM --platform=linux/amd64 python:3.11-buster as builder

# Update and upgrade the package list, install necessary packages, and clean up
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

FROM python:3.11-slim-buster as runtime

# Update
RUN apt-get update && rm -rf /var/lib/apt/lists/*
