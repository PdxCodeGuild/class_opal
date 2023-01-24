# Store your urls here.

from django.urls import path
# import everything from views so it's in scope
from .views import *

urlpatterns = [
    # retrieving from apis/views.py class
    path('', StudentAPIView.as_view()),
    # path represented as string
    path('new/', CreateStudent.as_view()),
    # accessing url at primary key to retrieve student's info.
    # This one is capable of handling 
    path('<int:pk>/', StudentView.as_view())
]