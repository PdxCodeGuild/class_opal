from django.urls import path
from . import views

app_name = 'url_manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate, name='generate'),
    path('redirect/<str:get_code>', views.redirect, name='redirect'),
]
