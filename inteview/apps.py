# apps.py

from django.apps import AppConfig


class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inteview'

    def ready(self):
        import inteview.signals

