from django.urls import reverse
from rest_framework import viewsets

from author.models import Author
from author.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    basename = "author: manage-list"
