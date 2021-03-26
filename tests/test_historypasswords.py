from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.test import TestCase

from securepasswords.utils import get_password_profile


class PasswordHistoryTest(TestCase):
    """
    This password history testcase assumes PASSWORD_HISTORY_LENGTH of 2
    """

    def setUp(self) -> None:
        settings.SECURE_PASSWORDS = {"PASSWORD_HISTORY_LENGTH": 2}
        foo = User(username="foo")
        foo.set_password("supercalifragilisticexpialidocious")
        foo.save()

    def test_a_set_new_password(self):
        foo = User.objects.get(username="foo")
        pw = "expialidocious"
        validate_password(pw, foo)
        foo.set_password(pw)
        foo.save()

    def test_b_reuse_password(self):
        foo = User.objects.get(username="foo")
        pw = "supercalifragilisticexpialidocious"
        with self.assertRaises(ValidationError):
            validate_password(pw, foo)

    def test_c_reuse_password_after_one(self):
        foo = User.objects.get(username="foo")
        # set a second
        pw = "expialidocious"
        validate_password(pw, foo)
        foo.set_password(pw)
        foo.save()
        with self.assertRaises(ValidationError):
            validate_password("supercalifragilisticexpialidocious", foo)

    def test_c_reuse_password_after_two(self):
        foo = User.objects.get(username="foo")
        # set a second
        pw = "expialidocious"
        validate_password(pw, foo)
        foo.set_password(pw)
        foo.save()
        # set a third
        pw = "superdocious"
        validate_password(pw, foo)
        foo.set_password(pw)
        foo.save()
        # forth password to be successful
        pw = "supercalifragilisticexpialidocious"
        validate_password(pw, foo)
        foo.set_password(pw)
        foo.save()

    def test_d_set_arthemetic_sequence_password(self):
        foo = User.objects.get(username="foo")
        pw = "abc33215def85"
        with self.assertRaises(ValidationError):
            validate_password(pw, foo)

    def test_d_set_ramdom_sequence_password(self):
        foo = User.objects.get(username="foo")
        pw = "slhik1453fg486"
        validate_password(pw, foo)
        foo.set_password(pw)
        foo.save()
        # set a one more random sequence
        pw = "ghup42895us471"
        validate_password(pw, foo)
        foo.set_password(pw)
        foo.save()
