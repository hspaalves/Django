from .models import Author, Book
from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer
from django_filters import rest_framework as filters


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    id = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Author
        fields = '__all__'


class BookFilterter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = '__all__'


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


