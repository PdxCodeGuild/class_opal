from django.urls import path
from .views import *

#from api/views

urlpatterns = [
    path('', ListStudents.as_view()),
    path('new/', CreateStudent.as_view()),
    path('<int:pk>/', StudentView.as_view())
]