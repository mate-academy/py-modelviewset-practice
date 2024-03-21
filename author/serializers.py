from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(max_value=100, min_value=1, )

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
