from django.shortcuts import render
from .models import Book

# Create your views here.
def getAllBooks(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {'libros': books})