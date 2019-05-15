#!/usr/bin/env bash
# PORT must be defined as an environment variable

if [ -z $PORT ]; then
    PORT=8080
fi

celery multi start w1 --app=celery_tasks.celery.celery_app --loglevel=info --config=celery_tasks.celery_settings;
gunicorn -c gunicorn.conf.py -b :$PORT "celery_tasks.app:app"