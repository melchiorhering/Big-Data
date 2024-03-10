# MAIN DSP IMAGE
FROM python:3.10-bullseye

# Update and upgrade the package list, install necessary packages, and clean up
RUN apt-get update && apt-get upgrade -y &&
    apt-get -y install git zsh curl sqlite3 python3-venv &&
    rm -rf /var/lib/apt/lists/*

# Install oh-my-zsh and the dieter theme
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" &&
    sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="dieter"/' /root/.zshrc &&
    usermod -s $(which zsh) $(whoami)

# Install pipx and prerequisites
RUN python3 -m pip install --upgrade pip &&
    pip install pipx &&
    python3 -m pipx ensurepath

# Install Poetry using pipx
RUN pipx install poetry

# Add pipx bin directory to PATH
ENV PATH="/root/.local/bin:$PATH"

# Disable creation of virtual environments by Poetry, as the container itself provides isolation
RUN poetry config virtualenvs.create false
