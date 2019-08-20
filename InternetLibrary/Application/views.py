from .models import Author, Book
from rest_framework import viewsets, generics, mixins
from .serializers import AuthorSerializer, BookSerializer, AuthorByBookSerializer
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


class BookDetailAPIView(viewsets.ModelViewSet):

    def get_queryset(self):
        return Book.objects.filter(author=self.kwargs['pk'])

    serializer_class = AuthorByBookSerializer
