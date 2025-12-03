from django.apps import AppConfig


class MyprojectConfig(AppConfig):   # <-- rename this
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myproject'             # <-- this is already correct
