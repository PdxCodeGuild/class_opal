from django.urls import path

from . import views

app_name = 'chirpapp'

urlpatterns = [
    path('', views.index, name='index')
    
]