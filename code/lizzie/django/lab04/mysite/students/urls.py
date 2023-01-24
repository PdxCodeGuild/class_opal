from django.urls import path
from .views import StudentListView

urlpatterns = [
    # root directory loads the class StudentListView in students/views.py
    path('', StudentListView.as_view(), name='student_list')
]