from django.urls import path

from . import views

app_name = 'url_manager'
urlpatterns = [
    path('', views.index, name='index'),
]
