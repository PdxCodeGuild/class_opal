from django.urls import path
from . import views

app_name = 'grocerylist_lab01'

urlpatterns = [
    path("", views.index, name='index'),
    path("add/", views.add, name='add'),
    path("complete/<int:pk>/", views.complete, name='complete'), #pk = primary key
    path("delete/<int:pk>/", views.delete, name='delete'), 
]