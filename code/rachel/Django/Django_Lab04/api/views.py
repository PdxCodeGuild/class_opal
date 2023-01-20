from rest_framework import generics
from students.models import Students
from .serializers import StudentsSerializer

class StudentsList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

    #last_name filter
    # def get_queryset(self):
    #     last_name = self.kwargs['last_name']
    #     return Students.objects.filter(last_name=last_name)

class StudentsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer