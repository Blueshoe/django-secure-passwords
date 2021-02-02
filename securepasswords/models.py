from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.hashers import check_password, is_password_usable
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PasswordProfile(models.Model):
    # do not clutter the user namespace
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="+")

    class Meta:
        verbose_name = _("password profile")
        verbose_name_plural = _("password profiles")

    def has_used_password(self, raw_password: str, last_n: int = None):
        history = self.password_history.all()  # ordered by descending date
        if last_n is not None:
            history = history[:last_n]
        return any(check_password(raw_password, password.encoded) for password in history)


class Password(models.Model):
    profile = models.ForeignKey(
        PasswordProfile, on_delete=models.CASCADE, related_name="password_history", editable=False
    )
    encoded = models.CharField(_("password"), max_length=128, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("password")
        verbose_name_plural = _("passwords")
        ordering = ["profile", "-created"]

    def __str__(self):
        return f"{self.profile.user}: {self.created}"
