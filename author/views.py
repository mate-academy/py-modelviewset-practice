from rest_framework import viewsets, mixins

from author.models import Author
from author.serializers import AuthorSerializer


class AuthorViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
