from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import site
from django.contrib.auth import views
from django.urls import include, path

from tests.testproject.views import home

urlpatterns = [
    path("admin/", site.urls),
    path("password_reset/", views.PasswordResetView.as_view(), name="admin_password_reset"),
    path("auth/password_change/", views.PasswordChangeView.as_view(template_name="registration/change_password.html"),
         name="admin_password_change"),
    path("auth/", include("django.contrib.auth.urls")),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path("", home),
]
