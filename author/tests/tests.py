from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from author.models import Author


class AuthorViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_list_authors(self):
        url = reverse('author:author-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)