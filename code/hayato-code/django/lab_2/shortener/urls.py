from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path for the home page
    path("", views.home),

    # path to redirect user
    path('<str:code>', views.redirect_user, name='redirect_user'),
]