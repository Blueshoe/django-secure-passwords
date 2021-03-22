from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

DEFAULTS = {
    "MAX_PASSWORD_AGE": (None, int),
    "PASSWORD_HISTORY_LENGTH": (None, int),
    "CHANGE_PASSWORD_URL": ("password_change", str),  # override may be view name or URL
    "RESET_PASSWORD_URL": ("password_reset", str),  # override may be view name or URL
}


class SecurePasswordConfig:
    def __init__(self):
        options = self.get_options()
        self.MAX_PASSWORD_AGE = options.get("MAX_PASSWORD_AGE", None)
        self.PASSWORD_HISTORY_LENGTH = options.get("PASSWORD_HISTORY_LENGTH", None)
        self.CHANGE_PASSWORD_URL = options.get("CHANGE_PASSWORD_URL", None)

    def get_options(self):
        options = {k: v[0] for k, v in DEFAULTS.items()}
        options.update(self.get_settings_overrides())
        return options

    def get_settings_overrides(self):
        overrides = getattr(settings, "SECURE_PASSWORDS", {})
        if not isinstance(overrides, dict):
            raise ImproperlyConfigured("'SECURE_PASSWORDS' settings must be a dictionary")
        for k, v in overrides.items():
            if k in DEFAULTS:
                type_ = DEFAULTS[k][1]
                if not isinstance(v, type_):
                    try:
                        overrides[k] = type_(v)
                    except (TypeError, ValueError):
                        raise ImproperlyConfigured(
                            f"SECURE_PASSWORDS setting '{k}' must be of type '{type_}' or omitted"
                        )
        return overrides


conf = SecurePasswordConfig()
