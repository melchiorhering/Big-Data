FROM --platform=linux/amd64 python:3.11-buster

# Update and upgrade the package list, install necessary packages, and clean up
RUN apt-get update && apt-get upgrade -y && apt-get -y install git zsh curl sqlite3 && rm -rf /var/lib/apt/lists/*

# Install oh-my-zsh and the dieter theme
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="dieter"/' /root/.zshrc && usermod -s $(which zsh) $(whoami)

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Update & Install NGINX
RUN apt-get update && rm -rf /var/lib/apt/lists/*

RUN poetry install --no-interaction --no-ansi --no-root
# poetry update --no-interaction

# Install IPython kernel - useful if you're running Jupyter inside the container
RUN poetry run ipython kernel install --user --name=DSP --display-name="BIG-DATA"

# Adds this repo to safe directories
RUN git config --global --add safe.directory /home/workspaces/BIG-DATA

# Keep the container running - this is a common pattern for Devcontainers
CMD tail -f /dev/null
