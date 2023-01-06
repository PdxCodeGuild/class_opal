from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView
app_name = 'chirpapp'

urlpatterns = [
    path('', PostListView.as_view(), name = 'home'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('<int:pk>/', PostDetailView.as_view(), name='user_posts')


]
