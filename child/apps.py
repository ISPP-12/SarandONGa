from django.apps import AppConfig


class ChildConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'child'
