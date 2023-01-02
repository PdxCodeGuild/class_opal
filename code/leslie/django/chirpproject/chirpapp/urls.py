from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView
app_name = 'chirpapp'

urlpatterns = [
    path('', PostListView.as_view(), name = 'home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail')


]
