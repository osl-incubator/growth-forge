#!/usr/bin/env bash
set -ex
poetry config virtualenvs.create false

pushd /opt/appfiles
if [[ "${ENV:-dev}" != "dev" ]]; then
  poetry install --no-root --only main
else
  poetry install --no-root
fi
popd
set +ex
