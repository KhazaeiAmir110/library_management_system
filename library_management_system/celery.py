from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_management_system.settings')
app = Celery('library_management_system')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
