from django.urls import path

from . import views

# Need to map view to URLconf to handle it.
urlpatterns = [
    path('', views.index, name='index'),
]
