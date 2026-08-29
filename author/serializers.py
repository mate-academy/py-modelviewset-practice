from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    pseudonym = serializers.CharField(
        min_length=0, max_length=64, required=False)
    age = serializers.IntegerField()
    retired = serializers.BooleanField()

    def validate_age(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError("Age must be a number")
        return value

    class Meta:
        model = Author
        fields = "__all__"
