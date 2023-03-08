from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    pseudonym = serializers.CharField(max_length=64, required=False)
    age = serializers.IntegerField()
    retired = serializers.BooleanField()
