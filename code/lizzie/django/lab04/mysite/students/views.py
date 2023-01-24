from django.shortcuts import render
from django.views.generic import ListView
from .models import Student

# Create your views here.
class StudentListView(ListView):
    # This felt familiar and I needed more practice so I included this from Danny's example (that I'm not copying, btw!!)
    # loads at root localhost:8000
    model = Student
    template_name = 'student_list.html'