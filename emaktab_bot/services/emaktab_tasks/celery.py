from celery import Celery

from config import CELERY_BROKER_URL

app = Celery(
    'emaktab_tasks', broker=CELERY_BROKER_URL,
    broker_connection_retry_on_startup=True,
    include=['emaktab_bot.services.emaktab_tasks.tasks']
)
