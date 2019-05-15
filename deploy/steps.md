First, we need a running broker

```bash
docker run --rm -p 6379:6379 redis
```



If the imports when running celery do not work as one expects, these problems can be 
solved specifying the tasks file via *CELERY_IMPORTS* inside the celery config file

```bash
celery --app=celery_tasks.celery.celery_app worker --loglevel=info --config=celery_tasks.celery_settings
```


If you want to run it in **production** (in a detached mode):

```bash
 celery multi start w1 --app=celery_tasks.celery.celery_app --loglevel=info --config=celery_tasks.celery_settings
```


For stopping the running celery workers **without waiting for the tasks** to complete:

```bash
celery multi stop w1 --app=celery_tasks.celery.celery_app --loglevel=info --config=celery_tasks.celery_settings
```

If you want to wait the task to complete, use the *stopwait*:

```bash
celery multi stopwait w1 --app=celery_tasks.celery.celery_app --loglevel=info --config=celery_tasks.celery_settings
```