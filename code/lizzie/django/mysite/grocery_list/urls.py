from django.urls import path

from . import views

# Need to map view to URLconf to handle it.
urlpatterns = [
    # ex: /grocery_item
    path('', views.index, name='index'),
    # ex: /grocery_item/5/
    path('<int:text_desc_id>/', views.detail, name='detail')
]
