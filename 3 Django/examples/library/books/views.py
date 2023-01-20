from django.shortcuts import render
from django.views.generic import ListView
from .models import Book


class BookListView(ListView):
    # You don't need this for the Students API lab!
    # This was just here so we could start with something familiar
    model = Book
    template_name = 'book_list.html'
