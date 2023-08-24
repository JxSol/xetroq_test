from typing import NoReturn

from django.core.management import call_command
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    """Заполняет таблицу тестовыми данными."""
    help = 'Fill database with initial data.'

    def handle(self, *args, **options) -> NoReturn:
        self.stdout.write('Loading test data...')

        fixtures = ['testdata.json']
        call_command('loaddata', *fixtures)

        self.stdout.write(self.style.SUCCESS('Test data loaded.'))
