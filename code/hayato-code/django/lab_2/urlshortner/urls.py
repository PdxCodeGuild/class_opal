from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # include shortner urls
    path("", include("shortener.urls"))
]
