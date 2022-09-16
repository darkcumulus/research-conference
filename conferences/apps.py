from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class ConferencesConfig(AppConfig):
    name = "conferences"


class SuitConfig(DjangoSuitConfig):
    layout = "horizontal"
