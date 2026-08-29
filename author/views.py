from rest_framework import viewsets

from author.models import Author
from author.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
