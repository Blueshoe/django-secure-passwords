from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import site
from django.urls import path

urlpatterns = [
    path("admin/", site.urls),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
