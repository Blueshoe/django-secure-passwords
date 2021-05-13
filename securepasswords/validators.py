from itertools import groupby
from typing import List

from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.utils.translation import gettext as _

from securepasswords.conf import conf
from securepasswords.utils import get_password_profile


class HistoryValidator:
    def __init__(self, last_n=None):
        self.last_n = last_n or conf.PASSWORD_HISTORY_LENGTH

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


class RepeatedCharValidator:
    def __init__(self, max_repetitions=2):
        self.n = max_repetitions

    def validate(self, raw_password, user=None):
        if any(len(list(g)) > self.n for _k, g in groupby(raw_password)):
            raise ValidationError(
                _("Your password contains more than {n} consecutive equal characters.").format(n=self.n),
                code="password_repeated_characters",
            )

    def get_help_text(self):
        return _("Your password must not contain more than {n} consecutive equal characters.").format(n=self.n)


class SequenceValidator:
    def __init__(self, max_length=2):
        self.n = max_length

    def _filter(self, char: str):
        return NotImplemented

    def _process(self, char: str):
        return NotImplemented

    def _get_error_text(self):
        return NotImplemented

    def validate(self, raw_password, user=None):
        for k, g in groupby(raw_password, key=self._filter):
            if k and self.has_sequence(list(map(self._process, g))):
                raise ValidationError(self._get_error_text())

    def has_sequence(self, seq: List) -> bool:
        check_length = self.n + 1
        for i in range(len(seq) - self.n):
            sub = seq[i : i + check_length]
            if len({a - b for a, b in zip(sub, sub[1:])}) == 1:
                return True
        return False


class ArithmeticSequenceValidator(SequenceValidator):
    def _filter(self, char: str):
        return char.isdigit()

    def _process(self, char: str):
        return int(char)

    def get_help_text(self):
        return _("Your password must not contain an arithmetic sequence ('456', '642', etc.) longer than {n}").format(
            n=self.n
        )

    def _get_error_text(self):
        return _("Your password contains an arithmetic sequence ('456', '642', etc.) longer than {n}").format(n=self.n)


class AlphabeticSequenceValidator(SequenceValidator):
    def __init__(self, max_length=3):
        super(AlphabeticSequenceValidator, self).__init__(max_length=max_length)

    def _filter(self, char: str):
        return char.isalpha()

    def _process(self, char: str):
        return ord(char)

    def get_help_text(self):
        return _("Your password must not contain an alphabetic sequence ('dcba', 'aceg', etc.) longer than {n}").format(
            n=self.n
        )

    def _get_error_text(self):
        return _("Your password contains an alphabetic sequence ('dcba', 'aceg', etc.) longer than {n}").format(
            n=self.n
        )


_char_class_tests = (str.isupper, str.islower, str.isdigit, str.isspace)


def ispunct(char: str):
    return not any(t(char) for t in _char_class_tests)


class CharacterClassValidator:
    TESTS = _char_class_tests + (ispunct,)

    def __init__(self, min_count: int = 2):
        if min_count not in range(2, 6):
            raise ImproperlyConfigured("The only valid 'min_count' arguments are 2, 3, 4, or 5")
        self.min_count = min_count

    def get_help_text(self):
        return _(
            "Your password must contain characters from at least {n} categories out of the following 5: "
            "Uppercase letters, lowercase letters, digits, punctuation, whitespace"
        ).format(n=self.min_count)

    def validate(self, raw_password, user=None):
        count = sum(any(map(test, raw_password)) for test in self.TESTS)
        if count < self.min_count:
            raise ValidationError(
                _(
                    "Your password contains characters from fewer than {n} categories out of the following 5: "
                    "Uppercase letters, lowercase letters, digits, punctuation, whitespace"
                ).format(n=self.min_count)
            )
