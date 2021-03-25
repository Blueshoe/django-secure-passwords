from typing import Optional

from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from securepasswords.models import Password, PasswordProfile


def get_password_profile(user: AbstractBaseUser) -> PasswordProfile:
    profile, created = PasswordProfile.objects.get_or_create(user=user)
    if created and user.has_usable_password():
        profile.password_history.create(encoded=user.password)
    return profile


def get_current_password_age(user: AbstractBaseUser) -> Optional[int]:
    """
    Return the age of the current password in days
    """
    profile = get_password_profile(user)
    last_password: Password = profile.password_history.first()
    if last_password:
        age = (timezone.now() - last_password.created).days
        return age
    return None
