"""social URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
    # add a project-level url for the accounts app above our included Django auth app. 
    # Django will look top to bottom for url patterns so when it sees a url route within 
    # our accounts app that matches one in the built-in auth app, it will choose the accounts route first.
    path("accounts/", include("accounts.urls")),
    # Including this auth app provides us with several authentication views and 
    # URLs for handling login, logout, and password management.
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('posts.urls'))
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
