from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from securepasswords.models import PasswordProfile


class ProfileInline(admin.StackedInline):
    model = PasswordProfile
    extra = 0
    fields = ("force_change",)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


user_model = get_user_model()
user_admin_class = admin.site._registry[user_model].__class__


class SecurePasswordUserAdmin(user_admin_class):
    actions = ["force_password_change"]

    def get_inlines(self, request, obj):
        inlines = super().get_inlines(request, obj)
        inlines.append(ProfileInline)
        return inlines

    def force_password_change(self, request, queryset):
        PasswordProfile.objects.filter(user__in=queryset).update(force_change=True)

    force_password_change.short_description = _("Force selected users to change their passwords")


admin.site.unregister(user_model)
admin.site.register(user_model, SecurePasswordUserAdmin)
