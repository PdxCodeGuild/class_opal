from rest_framework import generics
from students.models import Students
from .serializers import StudentsSerializer

# required views: create a student, retrieve list or specific student, edit a student, delete a student

class StudentsList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer