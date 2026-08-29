from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    pseudonym = serializers.CharField(required=False)
    age = serializers.IntegerField()
    retired = serializers.BooleanField()

    class Meta:
        model = Author
        fields = [
            "first_name", "last_name", "pseudonym", "age", "retired"
        ]
