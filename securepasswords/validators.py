from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from securepasswords.utils import get_password_profile


class HistoryValidator:
    def __init__(self, last_n=None):
        self.last_n = last_n

    def validate(self, raw_password, user=None):
        if not (user and user.pk):
            return
        password_profile = get_password_profile(user=user)
        if password_profile.has_used_password(raw_password=raw_password, last_n=self.last_n):
            raise ValidationError(
                _("You have used this password before."),
                code="password_reused",
            )

    def get_help_text(self):
        return _("You must not reuse a previous password.")
