from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.test import TestCase

from securepasswords.validators import AlphabeticSequenceValidator, ArithmeticSequenceValidator


class ArithmeticSequenceTest(TestCase):
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
            self.arithmetic_max_2(pw, self.user)
        except ValidationError:
            self.fail(f"'{pw}' should pass validation")

    def test_f_helptext(self):
        v3 = ArithmeticSequenceValidator(3)
        v5 = ArithmeticSequenceValidator(5)
        h3 = v3.get_help_text()
        h5 = v5.get_help_text()
        self.assertIn("longer than 3", h3)
        self.assertIn("longer than 5", h5)
        self.assertIn("Your password must not contain an arithmetic sequence", h3)
        self.assertIn("Your password must not contain an arithmetic sequence", h5)


class AlphabeticSequenceTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="foo")
        self.alphabetic_max_2 = AlphabeticSequenceValidator(2).validate
        self.alphabetic_max_4 = AlphabeticSequenceValidator(4).validate

    def test_a_alphabetic_sequence_validator_fail2(self):
        pw = "!zcdez!"
        self.failUnlessRaises(ValidationError, self.alphabetic_max_2, pw, self.user)

    def test_a_alphabetic_sequence_validator_pass4(self):
        pw = "!zcdez!"
        try:
            self.alphabetic_max_4(pw, self.user)
        except ValidationError:
            self.fail(f"'{pw}' should pass validation")

    def test_a_alphabetic_sequence_validator_fail4(self):
        pw = "!zcdefgz!"
        self.failUnlessRaises(ValidationError, self.alphabetic_max_4, pw, self.user)

    def test_b_alphabetic_sequence_validator_fail2(self):
        pw = "!zfedcz!"
        self.failUnlessRaises(ValidationError, self.alphabetic_max_2, pw, self.user)

    def test_b_alphabetic_sequence_validator_pass4(self):
        pw = "!zfedcz!"
        try:
            self.alphabetic_max_4(pw, self.user)
        except ValidationError:
            self.fail(f"'{pw}' should pass validation")

    def test_b_alphabetic_sequence_validator_fail4(self):
        pw = "!zfedcbz!"
        self.failUnlessRaises(ValidationError, self.alphabetic_max_4, pw, self.user)

    def test_c_alphabetic_sequence_validator_fail2(self):
        pw = "!zgecz!"
        self.failUnlessRaises(ValidationError, self.alphabetic_max_2, pw, self.user)

    def test_c_alphabetic_sequence_validator_pass4(self):
        pw = "!zgecz!"
        try:
            self.alphabetic_max_4(pw, self.user)
        except ValidationError:
            self.fail(f"'{pw}' should pass validation")

    def test_c_alphabetic_sequence_validator_fail4(self):
        pw = "!zigecaz!"
        self.failUnlessRaises(ValidationError, self.alphabetic_max_4, pw, self.user)

    def test_d_alphabetic_sequence_validator_fail2(self):
        pw = "!zbdfhz!"
        self.failUnlessRaises(ValidationError, self.alphabetic_max_2, pw, self.user)

    def test_d_alphabetic_sequence_validator_pass4(self):
        pw = "!zbdfhz!"
        try:
            self.alphabetic_max_4(pw, self.user)
        except ValidationError:
            self.fail(f"'{pw}' should pass validation")

    def test_d_alphabetic_sequence_validator_fail4(self):
        pw = "!zbdfhjz!"
        self.failUnlessRaises(ValidationError, self.alphabetic_max_4, pw, self.user)

    def test_e_arithmetic_sequence_validator_pass2(self):
        pw = "!abedfgih!"
        try:
            self.alphabetic_max_2(pw, self.user)
        except ValidationError:
            self.fail(f"'{pw}' should pass validation")

    def test_f_helptext(self):
        v3 = AlphabeticSequenceValidator(3)
        v5 = AlphabeticSequenceValidator(5)
        h3 = v3.get_help_text()
        h5 = v5.get_help_text()
        self.assertIn("longer than 3", h3)
        self.assertIn("longer than 5", h5)
        self.assertIn("Your password must not contain an alphabetic sequence", h3)
        self.assertIn("Your password must not contain an alphabetic sequence", h5)
