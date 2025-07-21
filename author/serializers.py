from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = [
            "id",
            "first_name",
            "last_name",
            "pseudonym",
            "age",
            "retired"
        ]
        read_only_fields = ["id"]
        extra_kwargs = {
            "first_name": {"max_length": 64},
            "last_name": {"max_length": 64},
            "pseudonym": {
                "max_length": 64,
                "allow_blank": True,
                "allow_null": True,
                "required": False
            },
        }
