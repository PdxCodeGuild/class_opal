from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'url_manager'
urlpatterns = [
    path('', views.TemplateView.as_view(
        template_name='index.html'), name='index'),
    path('generate/', views.generate, name='generate'),
    path('redirect/<str:get_code>', views.redirect, name='redirect'),
]
