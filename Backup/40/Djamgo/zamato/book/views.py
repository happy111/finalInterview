from django.shortcuts import render
from rest_framework.generics import(
        CreateAPIView,
        ListAPIView,
        UpdateAPIView,
        )
            
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer