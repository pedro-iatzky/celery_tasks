import functools
import traceback

import requests

from celery_tasks.common.util import PORT

LOGGER_URL = f"http://localhost:{PORT}/logger"


def execute_with_exception_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            exc = traceback.format_exc()
            json_msg = {
                "type": "ERROR",
                "message": f"exception when executing the task {str(exc)}"
            }
            requests.post(LOGGER_URL, json=json_msg)
    return wrapper
