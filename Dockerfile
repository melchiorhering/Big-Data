# Build stage
FROM --platform=linux/amd64 python:3.11-bookworm as builder

WORKDIR /workspaces/Big-Data

# Update and upgrade the package list, install necessary packages, and clean up
RUN apt-get update && apt-get -y install git zsh curl && rm -rf /var/lib/apt/lists/*

# Install oh-my-zsh and the dieter theme
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="dieter"/' /root/.zshrc && usermod -s $(which zsh) $(whoami)

# Copy your .zshrc file into the Docker container
COPY .zshrc /root/.zshrc

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi --no-root

# Install IPython kernel - useful if you're running Jupyter inside the container
RUN poetry run ipython kernel install --user --name=DSP --display-name="BIG-DATA"

# Runtime stage
FROM python:3.11-bookworm as runtime

WORKDIR /workspaces/Big-Data

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /root /root
COPY --from=builder /workspaces/Big-Data/.venv /workspaces/Big-Data/.venv

# Activate the virtual environment
ENV VIRTUAL_ENV=/workspaces/Big-Data/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY entrypoint.sh ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

# # Keep the container running - this is a common pattern for Devcontainers
# CMD tail -f /dev/null
