from django.core.management.base import BaseCommand
import hashlib
from api_keys.models import APIKey

# How to use:
# python manage.py delete_api_key api-key-to-remove


class Command(BaseCommand):
    help = 'Delete an existing API-key'

    def add_arguments(self, parser):
        parser.add_argument(
            'key', type=str, help='The API-key to delete (raw key as shown when created)'
        )

    def handle(self, *args, **kwargs):
        raw_key = kwargs['key']
        hashed_key = hashlib.sha256(raw_key.encode('utf-8')).hexdigest()

        try:
            api_key = APIKey.objects.get(key=hashed_key)
            api_key.delete()
            self.stdout.write(self.style.SUCCESS('API-key deleted successfully.'))
        except APIKey.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('API-key not found. Check the key and try again.')
            )
