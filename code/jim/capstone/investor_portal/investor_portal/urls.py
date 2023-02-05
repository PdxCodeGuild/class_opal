"""investor_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("research/", TemplateView.as_view(template_name="research.html"),
         name="research"),
    path("cash_flow/", TemplateView.as_view(template_name="cash_flow.html"),
         name="cash_flow"),
    path("admin/", admin.site.urls),
    path("personalized_index/", include("personalized_index.urls")),
    path("personalized_index/", include("django.contrib.auth.urls")),
    path('apis/v1/', include('apis.urls')),
    path('cash_flow/', include('cash_flow.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
