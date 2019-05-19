"""
    Here it can be defined the celery tasks that will be called then
    from the endpoints
"""
import datetime
import logging

from celery_tasks.celery import celery_app
from celery_tasks.common.helpers import execute_with_exception_logging
from celery_tasks.common.util import PORT

LOGGER_URL = f"http://localhost:{PORT}/logger"


@celery_app.task
@execute_with_exception_logging
def naive_test():
    logging.error("Testing if I can watch the error")
    raise ValueError


@celery_app.task
def write_to_file():
    with open("/tmp/celery_test", "w+") as fl:
        dt = datetime.datetime.now()
        fl.write(f"{str(dt)}: Hello world")
