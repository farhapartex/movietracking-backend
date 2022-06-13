from django.db import transaction
from rest_framework import serializers, status
from user import models
from core import exception


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=150)
    password = serializers.CharField()
    rapid_api_key = serializers.CharField()

    def validate(self, attrs):
        user_with_email = models.User.get_instance({"email": attrs["email"]})
        user_with_rapid_key = models.User.get_instance({"rapid_api_key": attrs["rapid_api_key"]})
        if user_with_email or user_with_rapid_key:
            raise exception.SerializerValidationError(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, field="email", detail="User exists with the provided email or rapid api key")
        return attrs

    def create(self, validated_data):
        validated_data["username"] = validated_data["email"]
        validated_data["is_active"] = True
        password = validated_data["password"]
        del validated_data["password"]
        with transaction.atomic():
            user = models.User.objects.create(**validated_data)
            user.set_password(password)
            user.save()
            return user

    def update(self, instance, validated_data):
        pass
