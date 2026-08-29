from rest_framework import viewsets
from author.models import Author
from author.serializers import AuthorSerializer


class AuthorViewsSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
