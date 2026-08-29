from rest_framework import serializers
from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    # write your code here
    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "last_name",
            "pseudonym",
            "age",
            "retired",
        )
