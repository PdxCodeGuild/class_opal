from rest_framework import generics
from students.models import Student
from .serializers import StudentSerializer

# Create your views here.


class StudentListAPI(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateStudent(generics.CreateAPIView):
    serializer_class = StudentSerializer


class StudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
