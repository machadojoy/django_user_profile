from django.db.models import signals
from .celery import app as celery_app

__all__ = ('celery_app',)