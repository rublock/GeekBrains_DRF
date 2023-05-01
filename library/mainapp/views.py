from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet


from mainapp.models import Book
from mainapp.serializers import BookSerializer


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
