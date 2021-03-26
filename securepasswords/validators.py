from itertools import groupby
from typing import List

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


class ArithmeticSequenceValidator:
    def __init__(self, max_length=2):
        self.n = max_length

    def validate(self, raw_password, user=None):
        for k, g in groupby(raw_password, key=str.isdigit):
            if k and self.is_arithemtic_sequence(list(map(int, g))):
                raise ValidationError(
                    _("Your password contains an arithmetic sequence ('456', '642', etc.) longer than {n}").format(
                        n=self.n
                    )
                )

    def get_help_text(self):
        return _("Your password must not contain an arithmetic sequence ('456', '642', etc.) longer than {n}").format(
            n=self.n
        )

    def is_arithemtic_sequence(self, seq: list[int]) -> bool:
        if len(seq) <= self.n:
            return False
        sublists = []
        loop = (len(seq) - (self.n + 1)) + 1
        for x in range(loop):
            sublists.append(seq[x:(x + (self.n + 1))])

        for sublist in sublists:
            if self.is_sublist_sequence(sublist):
                return True
        return False

    def is_sublist_sequence(self, sub: list[int]) -> bool:
        diff = sub[1] - sub[0]
        for index in range(len(sub) - 1):
            if not (sub[index + 1] - sub[index] == diff):
                return False
        return True
