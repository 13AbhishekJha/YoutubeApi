from celery import Celery

celery_app = None

celery_app = Celery(
        backend="redis://redis/0",
        broker="redis://redis/1"
    )