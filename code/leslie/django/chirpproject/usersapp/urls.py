from django.urls import path

from . import views

app_name = 'usersapp'

urlpatterns = [
    path('', views.index, name='index'),
    
]