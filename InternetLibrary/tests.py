import json
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from Application.models import Author, Book
from Application.serializers import AuthorSerializer, BookSerializer


class AuthorListCreateAPIViewTestCase(APITestCase):
    url = "http://0.0.0.0:8000/v1/author/"

    def setUp(self):
        self.name = "Anderson alves"
        self.message = ''

    def test_create_author(self):
        response = self.client.post(self.url, data={"name": "Testing name post!"})
        self.assertEqual(201, response.status_code)

    def test_authors(self):
        Author.objects.create(name=self.name)
        response = self.client.get(self.url)
        obj = json.loads(response.content)
        self.assertTrue(obj['count'] == Author.objects.count())
        self.message = 'Get Author', str(response.status_code)
        print('\n', self.message)

    def test_delete_author(self):
        self.test_create_author()
        obj = json.loads(self.client.get(self.url).content)['results'][0]

        self.url += str(obj['id'])+'/'
        response = self.client.delete(self.url)

        if self.assertTrue(status.HTTP_204_NO_CONTENT, response.status_code) is None:
            self.message = 'Delete author', status.HTTP_204_NO_CONTENT
        else:
            try:
                if self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code) is None:
                    self.message += 'Method Not Allowed. expected <id>'
            except Exception as exc:
                self.error = str(exc)
                self.message += 'Invalid parameter or path, error: ' + str(response.status_code)
        print('\n', self.message)


class BookListCreateAPIViewTestCase(APITestCase):
    url = "http://0.0.0.0:8000/v1/book/"

    def setUp(self):
        self.name = "My first Book"
        self.summary = "the best book"
        self.message = ''
        self.error = ''

    def test_create_books(self):
        response = self.client.post(self.url, data={"name": "Testing name post!", "summary": 'Testing summary'})
        self.assertEqual(201, response.status_code)

    def test_books(self):
        Book.objects.create(name=self.name, summary=self.summary)
        response = self.client.get(self.url)
        obj = json.loads(response.content)
        self.assertTrue(obj['count'] == Book.objects.count())
        self.message = 'Get Book', str(response.status_code)
        print('\n', self.message)

    def test_delete_books(self):
        self.test_create_books()
        obj = json.loads(self.client.get(self.url).content)['results'][0]

        self.url += str(obj['id'])+'/'
        response = self.client.delete(self.url)

        if self.assertTrue(status.HTTP_204_NO_CONTENT, response.status_code) is None:
            self.message = 'Delete Book', status.HTTP_204_NO_CONTENT
        else:
            try:
                if self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code) is None:
                    self.message += 'Method Not Allowed. expected <id>'
            except Exception as exc:
                self.error = str(exc)
                self.message += 'Invalid parameter or path, error: ' + str(response.status_code)
        print('\n', self.message)

    def test_filter_books(self):
        self.test_create_books()
        self.url += '?name=Testing'
        response = self.client.get(self.url)
        if response.status_code == status.HTTP_200_OK:
            self.message = 'successfully filtered', str(response.status_code)
        else:
            self.message = 'Error: ', str(response.status_code)
        print(self.message)
