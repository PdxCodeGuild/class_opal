from django.urls import path
from . import views

app_name = "url_short"

urlpatterns = [
    path('', views.urlCode, name='urlCode'),
    path("urlRedirect/<str:short_codes>", views.urlRedirect, name="urlRedirect"),
]
