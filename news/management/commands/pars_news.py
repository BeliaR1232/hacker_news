from django.core.management.base import BaseCommand

from news.models import InfoPost
from news.utils import save_data_in_db


class Command(BaseCommand):
    def handle(self, *args, **options):
        save_data_in_db(InfoPost)
