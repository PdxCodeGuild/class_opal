from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'), #.as_view & camelCase = specific to CBVs
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='detail'), #this view requires one variable; pk is used to only show details for the post w/ the right key
    path('post/new/', views.BlogCreateView.as_view(), name='new'),
    path('post/<int:pk>/edit', views.BlogEditView.as_view(), name='edit'),
    path('post/<int:pk>/delete', views.BlogDeleteView.as_view(), name='delete'),
]