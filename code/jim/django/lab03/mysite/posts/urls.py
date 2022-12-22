from django.urls import include, path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
]
