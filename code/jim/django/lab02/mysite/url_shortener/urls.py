from django.urls import path

from . import views

app_name = 'url_shortener'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<url>/', views.index, name='index'),
    path('submit_url/', views.submit_url, name='submit_url'),
    path('<str:code>/', views.redirect_user, name='redirect_user'),
]
