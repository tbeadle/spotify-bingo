#!/bin/bash

set -eo pipefail

if [ $# -eq 0 ]; then
    cd /app
    uv run python ./manage.py migrate
    uv run python ./manage.py collectstatic --no-input
    exec uv run gunicorn --bind 0.0.0.0:8000 proj.wsgi
else
    exec "$@"
fi

