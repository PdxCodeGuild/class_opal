from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateBook(generics.CreateAPIView):
    serializer_class = BookSerializer


# This replaces all three of the views below
class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# This View performs a GET on a single record
# class BookDetailView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class UpdateBook(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class DeleteBook(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
