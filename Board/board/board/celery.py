import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf:setting', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379/0'

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'action',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': (args),
    },
}
