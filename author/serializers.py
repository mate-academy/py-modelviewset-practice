from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=64, required=False)
    last_name = serializers.CharField(max_length=64, required=False)
    pseudonym = serializers.CharField(
        max_length=64,
        required=False,
        allow_null=True,
        allow_blank=True
    )
    age = serializers.IntegerField(required=False)
    retired = serializers.BooleanField(required=False)

    class Meta:
        model = Author
        fields = "__all__"

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name",
            instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name",
            instance.last_name
        )
        instance.pseudonym = validated_data.get(
            "pseudonym",
            instance.pseudonym
        )
        instance.age = validated_data.get("age", instance.age)
        instance.retired = validated_data.get("retired", instance.retired)
        instance.save()
        return instance
