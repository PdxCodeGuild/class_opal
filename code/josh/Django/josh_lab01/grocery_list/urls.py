from django.urls import path

from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
    # path('delete/', views.delete, name='delete')
    path('delete/<int:id>', views.delete, name='delete'),
]