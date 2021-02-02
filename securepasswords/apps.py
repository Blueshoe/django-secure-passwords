from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SecurePasswordsConfig(AppConfig):
    name = "securepasswords"
    verbose_name = _("secure passwords")
