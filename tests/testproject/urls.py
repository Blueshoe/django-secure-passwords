from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import site
from django.contrib.auth import views
from django.urls import include, path

#
# path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
# path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
#
# path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
# path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
# path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
# path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
#


urlpatterns = [
    path("admin/", site.urls),
    path("password_reset/", views.PasswordResetView.as_view(), name="admin_password_reset"),
    path("auth/", include("django.contrib.auth.urls")),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
