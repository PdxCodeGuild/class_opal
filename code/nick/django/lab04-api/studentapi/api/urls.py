from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentListAPI.as_view()),
    path('<int:pk>/', StudentView.as_view()),
    path('new/', CreateStudent.as_view()),
]
