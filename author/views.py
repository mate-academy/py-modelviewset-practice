from author.models import Author
from author.serializers import AuthorSerializer
from rest_framework import viewsets


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
