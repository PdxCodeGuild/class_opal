"""
apps module
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    name of app
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = 'users'
