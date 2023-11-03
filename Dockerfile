# FROM mcr.microsoft.com/devcontainers/base:${templateOption:imageVariant}
FROM node:18-bullseye-slim

COPY . .

ARG DEBIAN_FRONTEND=noninteractive
ARG USER=node

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \ 
    && apt-get install -y build-essential --no-install-recommends make \
        ca-certificates \
        git \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        xz-utils \
        tk-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev
# Shap/llvm-lite dependency
RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y llvm-dev
# Git LFS
RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y git-lfs
# Python and poetry installation
USER $USER
ARG HOME="/home/$USER"
# ARG PYTHON_VERSION=${templateOption:pythonVersion}
ARG PYTHON_VERSION=3.11

ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:$PATH"

RUN echo "Starting pyenv download" \
    && curl https://pyenv.run | bash \
    && echo "Installing Python" \
    && pyenv install ${PYTHON_VERSION} \
    && echo "Setting python version as global" \
    && pyenv global ${PYTHON_VERSION} \
    && echo "downloading Poetry" \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.in-project true

RUN git lfs install

RUN poetry install

WORKDIR /src

RUN poetry run python manage.py tailwind install
RUN poetry run python manage.py collectstatic --no-input
RUN poetry run python manage.py migrate

ENTRYPOINT [ "gunicorn", "--bind", "159.223.222.199:8001" ]