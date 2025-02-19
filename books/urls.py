from django.contrib import admin
from django.urls import path
from .views import getAllBooks

urlpatterns = [
    path('', getAllBooks, name='books'),
]