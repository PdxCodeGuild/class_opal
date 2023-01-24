from rest_framework import generics
from api.models import Student
from .serializers import StudentSerializer

class ListStudents(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CreateStudent(generics.CreateAPIView):
    serializer_class = StudentSerializer

class StudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

