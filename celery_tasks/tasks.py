"""
    Here it can be defined the celery tasks that will be called then
    from the endpoints
"""
import datetime
import logging

import requests

from celery_tasks.celery import celery_app
from celery_tasks.util import PORT

LOGGER_URL = f"http://localhost:{PORT}/logger"


@celery_app.task
def naive_test():
    try:
        logging.error("Testing if I can watch the error")
        raise ValueError
    except ValueError as e:
        json_msg = {
            "type": "ERROR",
            "message": f"exception when executing the task {str(e)}"
        }
        requests.post(LOGGER_URL, json=json_msg)
    return "Hello world!"


@celery_app.task
def write_to_file():
    with open("/tmp/celery_test", "w+") as fl:
        dt = datetime.datetime.now()
        fl.write(f"{str(dt)}: Hello world")
