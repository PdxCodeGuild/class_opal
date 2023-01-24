from rest_framework import generics
from students.models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentAPIView(generics.ListAPIView):
    # retrieving everything on the student object
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateStudent(generics.CreateAPIView):
    # instating StudentSerializer class
    serializer_class = StudentSerializer


# handles all three: retrieve, update, destroy functionality on same page
class StudentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer