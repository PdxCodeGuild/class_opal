from django.urls import path

from . import views

# Need to map view to URLconf to handle it.
app_name = 'grocery_list'
urlpatterns = [
    # ex: /grocery_item
    path('', views.index, name='index'),
    # ex: /grocery_item/5/
    path('<int:text_desc_id>/', views.detail, name='detail'),
    path('add_item/', views.add_item, name='add_item'),
    path('delete_item/', views.delete_item, name='delete_item'),
    path('complete_item/', views.complete_item, name='complete_item'),
    path('incomplete_item/', views.incomplete_item, name='incomplete_item'),
]
