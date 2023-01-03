from django.urls import path, include
from .views import home, add_post, delete_post

urlpatterns = [
    path('', home, name="home"),
    path('add-post/', add_post, name="add_post"),
    path("delete-post/<int:pk>/",delete_post, name="delete_post"),
]
