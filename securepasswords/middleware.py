from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext as _

from .conf import conf
from .utils import get_current_password_age


class SecurePasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if conf.MAX_PASSWORD_AGE is not None:
            age = get_current_password_age(request.user)
            if age is not None and age < conf.MAX_PASSWORD_AGE:
                messages.info(
                    request, _("Your current password is older than {max_age}. Please change your password now.")
                )
                return redirect(conf.CHANGE_PASSWORD_URL)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
