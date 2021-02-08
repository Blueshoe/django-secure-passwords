from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SecurePasswordsConfig(AppConfig):
    name = "securepasswords"
    verbose_name = _("secure passwords")

    def ready(self):
        super(SecurePasswordsConfig, self).ready()
        from .signal_handlers import password_history_update  # noqa
