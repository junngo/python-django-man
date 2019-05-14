from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "memo.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import memo.users.signals  # noqa F401
        except ImportError:
            pass
