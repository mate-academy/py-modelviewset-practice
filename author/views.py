from rest_framework import viewsets, mixins
from author.models import Author
from author.serializers import AuthorSerializer


class AuthorViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
