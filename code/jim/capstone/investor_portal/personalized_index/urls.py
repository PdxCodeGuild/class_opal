from django.urls import path

from django.views.generic.base import TemplateView
from .views import SignUpView

urlpatterns = [
    path("", TemplateView.as_view(
        template_name="personalized_index.html"), name="personalized_index"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
