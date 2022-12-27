from django.urls import path

from . import views

app_name = 'url_shortener'
urlpatterns = [
    path('redirect/<int:id>', views.redirect, name='redirect')
    path('', views.index, name='index'),
]