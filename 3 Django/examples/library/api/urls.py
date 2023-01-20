from django.urls import path
from .views import *

urlpatterns = [
    path('', BookAPIView.as_view()),
    path('new/', CreateBook.as_view()),
    # path('<int:pk>/', BookDetailView.as_view()),
    # path('<int:pk>/update', UpdateBook.as_view()),
    # path('<int:pk>/delete', DeleteBook.as_view()),
    # ^ These three can be replaced by a single View
    # that handles all three methods (GET, PUT, and DELETE)
    path('<int:pk>/', BookView.as_view()),
]
