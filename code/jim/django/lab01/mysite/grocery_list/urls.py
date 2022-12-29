from django.urls import path

from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('delete_item/', views.delete_item, name='delete_item'),
    path('mark_complete/', views.mark_complete, name='mark_complete'),
    path('mark_incomplete/', views.mark_incomplete, name='mark_incomplete'),
]
