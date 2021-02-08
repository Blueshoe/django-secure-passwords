from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from securepasswords.utils import get_password_profile

__all__ = [
    "password_history_update",
]


@receiver(post_save, sender=get_user_model())
def password_history_update(sender, **kwargs):
    user = kwargs["instance"]
    update_fields = kwargs.get("update_fields", [])
    if not update_fields or "password" in update_fields:
        profile = get_password_profile(user)
        latest_password = profile.password_history.latest("created")
        if not latest_password or latest_password.encoded != user.password:
            profile.password_history.create(encoded=user.password)
