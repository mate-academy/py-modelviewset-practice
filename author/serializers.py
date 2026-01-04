from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
