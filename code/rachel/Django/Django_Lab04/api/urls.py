from django.urls import path
from .views import StudentsList, StudentsDetails

urlpatterns = [
    path('', StudentsList.as_view()),
    path('<int:pk>/', StudentsDetails.as_view()),
]
