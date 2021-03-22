from typing import Optional

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from securepasswords.models import PasswordProfile
from securepasswords.utils import get_password_profile

__all__ = [
    "password_history_update",
]


@receiver(post_save, sender=get_user_model())
def password_history_update(sender, **kwargs):
    profile = _password_changed(kwargs)
    if profile:
        profile.password_history.create(encoded=profile.user.password)
        profile.force_change = False
        profile.save(update_fields=("force_change",))


def _password_changed(signal_kwargs) -> Optional[PasswordProfile]:
    update_fields = signal_kwargs.get("update_fields", [])
    if not update_fields or "password" in update_fields:
        user = signal_kwargs["instance"]
        profile = get_password_profile(user)
        latest_password = profile.password_history.latest("created")
        if not latest_password or latest_password.encoded != user.password:
            return profile
