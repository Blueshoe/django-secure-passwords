from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.test import TestCase

from securepasswords.validators import ArithmeticSequenceValidator


class PasswordHistoryTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="foo")
        self.arithmetic_max_2 = ArithmeticSequenceValidator(2).validate
        self.arithmetic_max_4 = ArithmeticSequenceValidator(4).validate

    def test_a_arithmetic_sequence_validator_fail2(self):
        pw = "random512341random"
        self.failUnlessRaises(ValidationError, self.arithmetic_max_2, pw, self.user)

    def test_a_arithmetic_sequence_validator_pass4(self):
        pw = "random512341random"
        try:
            self.arithmetic_max_4(pw, self.user)
        except ValidationError:
            self.fail(f"'{pw}' should pass validation")

    def test_a_arithmetic_sequence_validator_fail4(self):
        pw = "random5123451random"
        self.failUnlessRaises(ValidationError, self.arithmetic_max_4, pw, self.user)

    def test_b_arithmetic_sequence_validator_fail2(self):
        pw = "random15437random"
        self.failUnlessRaises(ValidationError, self.arithmetic_max_2, pw, self.user)

    def test_b_arithmetic_sequence_validator_pass4(self):
        pw = "random15437random"
        try:
            self.arithmetic_max_4(pw, self.user)
        except ValidationError:
            self.fail(f"'{pw}' should pass validation")

    def test_b_arithmetic_sequence_validator_fail4(self):
        pw = "random1543217random"
        self.failUnlessRaises(ValidationError, self.arithmetic_max_4, pw, self.user)

    def test_c_arithmetic_sequence_validator_fail2(self):
        pw = "random186427random"
        self.failUnlessRaises(ValidationError, self.arithmetic_max_2, pw, self.user)

    def test_c_arithmetic_sequence_validator_pass4(self):
        pw = "random186427random"
        try:
            self.arithmetic_max_4(pw, self.user)
        except ValidationError:
            self.fail(f"'{pw}' should pass validation")

    def test_c_arithmetic_sequence_validator_fail4(self):
        pw = "random1864207random"
        self.failUnlessRaises(ValidationError, self.arithmetic_max_4, pw, self.user)

    def test_d_arithmetic_sequence_validator_fail2(self):
        pw = "random35791random"
        self.failUnlessRaises(ValidationError, self.arithmetic_max_2, pw, self.user)

    def test_d_arithmetic_sequence_validator_pass4(self):
        pw = "random35791random"
        try:
            self.arithmetic_max_4(pw, self.user)
        except ValidationError:
            self.fail(f"'{pw}' should pass validation")

    def test_d_arithmetic_sequence_validator_fail4(self):
        pw = "random4135791random"
        self.failUnlessRaises(ValidationError, self.arithmetic_max_4, pw, self.user)

    def test_e_arithmetic_sequence_validator_pass2(self):
        pw = "random124367random"
        try:
            validate_password(pw, self.user)
        except ValidationError:
            self.fail(f"'{pw}' should pass validation")
