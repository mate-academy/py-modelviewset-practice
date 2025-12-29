from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    pseudonym = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )

    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "last_name",
            "pseudonym",
            "age",
            "retired"
        )
        read_only_fields = ("id",)
