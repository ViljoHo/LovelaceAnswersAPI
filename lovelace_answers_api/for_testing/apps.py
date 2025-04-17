from django.apps import AppConfig


class ForTestingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'for_testing'
