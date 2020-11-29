from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(selfself):
        import users.signals
