from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    # write your code here
    class Meta:
        model = Author
        fields = "__all__"
