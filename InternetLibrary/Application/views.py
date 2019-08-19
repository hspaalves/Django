from .models import Author, Book
from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer
from django_filters import rest_framework as filters
from .filters import AuthorFilter, BookFilterter


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AuthorFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BookFilterter


