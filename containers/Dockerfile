# ref: https://github.com/mamba-org/micromamba-docker/blob/main/Dockerfile

FROM condaforge/mambaforge:latest

LABEL maintainer="Ivan Ogasawara <ivan.ogasawara@gmail.com>"
LABEL org.opencontainers.image.title="Feedback Linker"
LABEL org.opencontainers.image.authors="Feedback Linker Team"
LABEL org.opencontainers.image.source="https://github.com/xmnlab/feedback-linker.git"
LABEL org.opencontainers.image.version="latest"
LABEL org.opencontainers.image.description="The main objective of this platform is to offer a space to handle and organize feedback between two people"

# it is the default, but using it here to have it explicitly
USER root

SHELL ["/bin/bash", "-c"]

# Use bash in Dockerfile RUN commands and make sure bashrc is sourced when
# executing commands with /bin/bash -c
# Needed to have the micromamba activate command configured etc.

ENV ENV_NAME=feedback_linker
ENV DEBIAN_FRONTEND=noninteractive
ARG UID=1000
ARG GID=1000

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-utils \
        build-essential \
        curl \
        git \
        libffi-dev \
        libldap2-dev \
        libpq-dev \
        libsasl2-dev \
        libssl-dev \
        locales \
        postgresql-client \
        vim && \
    rm -rf /var/lib/apt/lists/*

USER feedback_linker

WORKDIR /feedback-linker

COPY pyproject.toml .

# Create and copy virtual environment: Poetry is configured not to create a new
# virtual environment and necessary dependencies are installed without
# development packages

RUN mamba install -y poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi


COPY . /feedback-linker/

COPY . .

COPY compose.yaml .

CMD ["python", "feedback_linker.py"]
