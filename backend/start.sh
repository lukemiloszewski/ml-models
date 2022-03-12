#! /usr/bin/env sh
set -e
exec gunicorn main:app --worker-class "uvicorn.workers.UvicornWorker" --config "gunicorn_conf.py"
