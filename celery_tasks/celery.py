from celery import Celery

try:
    from celery_tasks.config import config
except ImportError:
    raise ImportError("No config file was found. Please, create the file")

CELERY_BROKER = config.CELERY_BROKER

# TODO: solve the issue for redis not closing the connections. We may lose performance?
celery_app = Celery("background_tasks", broker=CELERY_BROKER, backend=CELERY_BROKER)


if __name__ == "_main":
    celery_app.start()
