from django.contrib.auth.models import User
from django.test import TestCase

from securepasswords.models import PasswordProfile
from securepasswords.utils import get_current_password_age


class TestSecureUtils(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            username="util",
            is_active=True
        )
        self.user.set_password("test")

    def test_get_password_age(self):
        self.assertEqual(0, get_current_password_age(self.user))

    def test_get_password_age_not_available(self):
        profile = PasswordProfile.objects.get(user=self.user)
        profile.password_history.all().delete()
        self.assertEqual(None, get_current_password_age(self.user))
