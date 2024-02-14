from rest_framework import viewsets
from author.serializers import AuthorSerializer
from author.models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()