from django.db import transaction
from rest_framework import serializers, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user import models
from core import exception


class UserAuthTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = {
            "username": self.user.username
        }

        return data


class UserRegistrationSerializer(serializers.Serializer):
    first_name = serializers.RegexField(regex=r"^(?=.{1,40}$)[a-zA-Z]+(?:[-'\s][a-zA-Z]+)*$")
    last_name = serializers.RegexField(regex=r"^(?=.{1,40}$)[a-zA-Z]+(?:[-'\s][a-zA-Z]+)*$")
    email = serializers.EmailField(required=True, max_length=150)
    password = serializers.CharField()

    def validate(self, attrs):
        user_with_email = models.User.get_instance({"username": attrs["email"]})
        if user_with_email:
            raise exception.SerializerValidationError(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, field="email", detail="User exists with the provided email")
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
