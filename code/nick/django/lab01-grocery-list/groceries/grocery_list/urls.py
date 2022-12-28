from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/delete', views.delete, name='delete'),
    path('<int:item_id>/completer', views.completer, name='completer'),
]
