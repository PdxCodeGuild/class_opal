from django.urls import path, include

from . import views

app_name = "posts"

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'), #.as_view & camelCase = specific to CBVs
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='detail'), #this view requires one variable; pk is used to only show details for the post w/ the right key
]