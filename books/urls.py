from django.contrib import admin
from django.urls import path
from .views import getAllBooks, createBook, updateBook, deleteBook

urlpatterns = [
    path('', getAllBooks, name='books'),
    path('create/', createBook, name='createBook'),
    path('update/<int:id>/', updateBook, name='updateBook'),
    path('delete/<int:id>/', deleteBook, name='deleteBook'),
]