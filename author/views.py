from rest_framework.viewsets import ModelViewSet

from author.models import Author
from author.serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
