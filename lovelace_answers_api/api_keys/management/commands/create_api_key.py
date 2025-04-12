from django.core.management.base import BaseCommand
import uuid
import hashlib
from api_keys.models import APIKey

# How to use:
# python manage.py create_api_key api-key-level
# api-key-level = (read, write, admin)

class Command(BaseCommand):
    help = 'Create new API-key with different levels'

    def add_arguments(self, parser):
        parser.add_argument(
            'level',
            choices=['read', 'write', 'admin'],
            help="level of API-key",
        )

    def handle(self, *args, **kwargs):
        level = kwargs['level']

        raw_key = uuid.uuid4().hex

        hashed_key = hashlib.sha256(raw_key.encode('utf-8')).hexdigest()

        APIKey.objects.create(key=hashed_key, level=level)

        self.stdout.write(
            self.style.SUCCESS(f'A new API-key with level {level} created: {raw_key}')
        )
        self.stdout.write("Note: This key is displayed only once. Save it safely!")
