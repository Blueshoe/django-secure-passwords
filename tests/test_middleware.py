from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from securepasswords.middleware import conf
from securepasswords.models import PasswordProfile


class SecurePasswordMiddlewareTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create(username="blueshoe", is_active=True)
        cls.user.set_password("supersecret")
        cls.user.save()
        cls.profile = PasswordProfile.objects.get(user=cls.user)
        cls.profile.force_change = True
        cls.profile.save()

        cls.user2 = User.objects.create(username="blueshoe2", is_active=True)
        cls.user2.set_password("supersecret")
        cls.user2.save()

        cls.profile2 = PasswordProfile.objects.get(user=cls.user2)
        cls.profile2.force_change = False
        cls.profile2.save()
        for password in cls.profile2.password_history.all():
            password.created = timezone.datetime(2000, 1, 1, 0, 0, 0, 0)
            password.save()

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def test_unauthenticated_user(self):
        # request simply passes through middleware
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_force_password_change(self):
        # authenticated users with force_change in their PasswordProfile
        # need to be redirected to the password change view
        self.client.login(username="blueshoe", password="supersecret")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(reverse("password_change"), response.url)

    def test_authenticated_user_old_password(self):
        # authenticated users with old password
        # need to be redirected to the password change view
        self.client.login(username="blueshoe2", password="supersecret")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(reverse("password_change"), response.url)

    def test_authenticated_user_external_redirect(self):
        # authenticated users with force_change in their PasswordProfile
        # need to be redirected to the external password change view
        conf.CHANGE_PASSWORD_URL = "/somewhere"
        self.client.login(username="blueshoe2", password="supersecret")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(conf.CHANGE_PASSWORD_URL, response.url)
        conf.CHANGE_PASSWORD_URL = "password_change"
