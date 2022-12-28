from django.urls import path
from . import views

app_name = 'urlapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('createshorturl/', views.createshorturl, name='createshorturl'), #type:ignore
    path('url_created/', views.url_created, name='url_created'),
    path('<str:short_code>/', views.redirect, name='redirect')


]
