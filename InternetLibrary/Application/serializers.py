from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        model = Book
        fields = ['name', 'summary', 'author']


class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True, many=True)

    class Meta:
        model = Author
        fields = ['name', 'book']
