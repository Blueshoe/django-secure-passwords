from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class HistoryValidator:
    def __init__(self, n_most_recent=None):
        self.n_most_recent = n_most_recent

    def validate(self, password, user=None):
        valid = True
        # TODO
        if not valid:
            raise ValidationError(
                _("You have used this password before."),
                code="password_reused",
            )

    def get_help_text(self):
        return _("You must not reuse a previous password.")
