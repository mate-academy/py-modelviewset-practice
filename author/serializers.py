from rest_framework import serializers, viewsets

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"
