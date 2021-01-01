from django.contrib.admin import site
from django.urls import path


urlpatterns = [
    path("admin/", site.urls),
]
