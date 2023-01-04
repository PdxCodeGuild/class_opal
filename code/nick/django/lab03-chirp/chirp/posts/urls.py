from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('like/', views.like, name='like'),
    path('comments/', views.like, name='comments'),
]
