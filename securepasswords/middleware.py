from django.contrib import messages
from django.shortcuts import redirect
from django.urls import NoReverseMatch, reverse
from django.utils.translation import ugettext as _

from .conf import conf
from .utils import get_password_profile


class SecurePasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_path = request.get_full_path()
            try:
                allowed_path = reverse(conf.CHANGE_PASSWORD_URL)
            except NoReverseMatch:
                allowed_path = conf.CHANGE_PASSWORD_URL
            if current_path != allowed_path:
                profile = get_password_profile(request.user)
                if profile.force_change:
                    messages.info(request, _("You must change your password for security reasons!"))
                    return redirect(conf.CHANGE_PASSWORD_URL)

                if conf.MAX_PASSWORD_AGE is not None:
                    age = profile.password_age()
                    if age is not None and age > conf.MAX_PASSWORD_AGE:

                        messages.info(
                            request,
                            _(
                                "Your current password is older than {max_age} days. "
                                "Please change your password now."
                            ).format(max_age=conf.MAX_PASSWORD_AGE),
                        )
                        return redirect(conf.CHANGE_PASSWORD_URL)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
