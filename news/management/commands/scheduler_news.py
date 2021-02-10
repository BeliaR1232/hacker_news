from datetime import datetime

import django_rq
from django_rq.management.commands import rqscheduler

from news.models import InfoPost
from news.utils import save_data_in_db


scheduler = django_rq.get_scheduler('default')


def clear_scheduled_jobs():
    # Удаляет все существующие задания в планировщике
    for job in scheduler.get_jobs():
        job.delete()


def register_scheduled_jobs():
    # Описание планирования и регистрация планировщика.
    scheduler.schedule(scheduled_time=datetime.utcnow(),
                       func=save_data_in_db,
                       args=[InfoPost],
                       interval=60 * 60)  # установка времени повторения задачи(в секундах!!!),
    # по умолчанию повторение каждый час,
    # 60 * n, где n минуты!


class Command(rqscheduler.Command):
    def handle(self, *args, **kwargs):
        clear_scheduled_jobs()
        register_scheduled_jobs()
        super(Command, self).handle(*args, **kwargs)
