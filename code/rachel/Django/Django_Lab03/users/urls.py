from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile'), # tie to user, not pk (since user is how it will be looked-up)
]