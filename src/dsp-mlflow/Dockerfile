# Use an official Python runtime as a parent image
FROM python:3.10-slim as builder

# Update and upgrade the package list, install prerequisites, and clean up
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl python3-venv && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install pipx
RUN python3 -m pip install --upgrade pip && pip install pipx && python3 -m pipx ensurepath

# Install Poetry using pipx
RUN pipx install poetry

# Disable creation of virtual environments by Poetry, as the container itself provides isolation
RUN poetry config virtualenvs.create false

# Start a new stage for the runtime
FROM python:3.10-slim

# Copy the pipx binaries from the builder stage
COPY --from=builder /root/.local /root/.local

# Add pipx bin directory to PATH
ENV PATH="/root/.local/bin:$PATH"
