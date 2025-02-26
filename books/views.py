from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response 
from .models import Book
from .serializer import BookSerializer
from rest_framework.decorators import api_view
from .forms import formBook

from .serializer import BookSerializer

# Create your views here.
@api_view(['GET'])
def getAllBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
    # return render(request, 'books/books.html', {'libros': books})

@api_view(['POST'])
def createBook(request):
    if request.method == 'POST':
        form = formBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else: 
        form = formBook()
    return render(request, 'books/createBook.html', {'form': form})

@api_view(['PUT'])
def updateBook(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'PUT':
        form = formBook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else: 
        form = formBook(instance=book)
    return render(request, 'books/updateBook.html', {'form': form, 'libro':book})

@api_view(['DELETE'])
def deleteBook(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'DELETE':
        book.delete()
        return redirect('books')
    return render(request, 'books/deleteBook.html', {'libro': book})
