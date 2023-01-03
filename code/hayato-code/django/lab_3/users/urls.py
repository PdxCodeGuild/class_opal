"""
authentication urls
"""

# app_name = "authentication"
from django.shortcuts import redirect
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register/', views.register, name="register"),
    path('<int:pk>/', views.profile, name="profile"),
    path('login_redirect/', views.login_redirect, name="login_redirect")
]
