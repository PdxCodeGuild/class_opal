from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_url/', views.submit_url, name='submit_url'),
    # Use string representation of code
    path('<str:code>/', views.redirect_user, name='redirect_user'),
]