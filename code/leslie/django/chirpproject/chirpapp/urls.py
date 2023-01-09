from django.urls import path
from . import views
from .views import PostListView, PostCreateView
app_name = 'chirpapp'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),


]
