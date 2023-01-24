from django.urls import path
from .views import *

app_name = 'students'
urlpatterns = [
    path('', StudentAPIView.as_view()),
    path('new/', CreateStudent.as_view()),
    path('<int:pk>/', StudentView.as_view()),
]