from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    pseudonym = serializers.CharField(required=False, max_length=64)

    class Meta:
        model = Author
        fields = [
            "id",
            "first_name",
            "last_name",
            "pseudonym",
            "age",
            "retired",
        ]
