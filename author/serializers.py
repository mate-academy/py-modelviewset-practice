from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    pseudonym = serializers.CharField(
        max_length=64, allow_blank=True, required=False)
    age = serializers.IntegerField()
    retired = serializers.BooleanField()
