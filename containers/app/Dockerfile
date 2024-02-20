# ref: https://github.com/mamba-org/micromamba-docker/blob/main/Dockerfile

FROM condaforge/mambaforge:latest

LABEL maintainer="Ivan Ogasawara <ivan.ogasawara@gmail.com>"
LABEL org.opencontainers.image.title="LiteRev"
LABEL org.opencontainers.image.authors="LiteRev Team"
LABEL org.opencontainers.image.source="https://github.com/thegraphnetwork-app/LiteRev"
LABEL org.opencontainers.image.version="latest"
LABEL org.opencontainers.image.description="LiteRev"
LABEL org.thegraphnetwork.config.version="latest"

# it is the default, but using it here to have it explicitly
USER root

SHELL ["/bin/bash", "-c"]
# Use bash in Dockerfile RUN commands and make sure bashrc is sourced when
# executing commands with /bin/bash -c
# Needed to have the micromamba activate command configured etc.

ENV ENV_NAME=growth-plan-linker
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
ARG UID=1000
ARG GID=1000

RUN apt-get update -y \
  && apt-get install -y \
    apt-utils \
    build-essential \
    curl \
    tini \
    nginx \
    snapd \
    sudo \
    tzdata \
    gcc-multilib \
    g++-multilib \
    openssl \
  && rm -rf /var/lib/apt/lists/* \
    /var/cache/apt/archives \
    /tmp/*

RUN addgroup --gid ${GID} app \
  && useradd --uid ${UID} --gid ${GID} -ms /bin/bash app \
  && mkdir -p /app \
  && mkdir -p /opt/appfiles \
  && chmod -R a+rwx /opt/conda /app /opt/appfiles \
  && export ENV_NAME="$ENV_NAME" \
  && chown app:app /app /opt/appfiles \
  && echo "app ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/app \
  && chmod 0440 /etc/sudoers.d/app

USER app

WORKDIR /app

COPY --chown=app:app ./conda/ /tmp/conda
# COPY --chown=app:app ./.github/workflows/.condarc /home/app/.condarc

ARG HTTP_PROXY
ARG HTTPS_PROXY

RUN mamba env create -n $ENV_NAME --file /tmp/conda/dev.yaml \
  && conda clean --all \
  && find /opt/conda/ -type f,l -name '*.pyc' -delete \
  && find /opt/conda/ -type f,l -name '*.js.map' -delete \
  && rm -rf /opt/conda/pkgs /tmp/*

ENV CONDA_PREFIX /opt/conda/envs/$ENV_NAME
ENV PATH ${CONDA_PREFIX}/bin:$PATH

# install dependencies
COPY --chown=app:app pyproject.toml poetry.lock /opt/appfiles
COPY --chown=app:app containers/app/scripts/install-deps.sh /opt/appfiles/install-deps.sh

ARG ENV=prod

RUN /opt/appfiles/install-deps.sh

COPY --chown=app:app containers/app/scripts/entrypoint.sh /opt/appfiles/entrypoint.sh
COPY --chown=app:app src/ /app

# copy start script
COPY --chown=app:app containers/app/scripts/start.sh /opt/appfiles/start.sh

RUN chmod +x /opt/appfiles/start.sh \
  && chmod +x /opt/appfiles/entrypoint.sh \
  && echo "source /opt/appfiles/entrypoint.sh" > ~/.bashrc


ENV PYTHONPATH='/app'

ENTRYPOINT ["tini", "--", "/opt/appfiles/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
