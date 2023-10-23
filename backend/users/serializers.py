from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password


class CreateAccountSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = UserAccount
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "department_id",
            "role_id",
        )

    def validate(self, attrs):
        user = UserAccount(**attrs)
        password = user.password
        validate_password(password, user)
        return attrs

    def create(self, validated_data):
        try:
            first_name = validated_data["first_name"]

        except:
            first_name = ""
        try:
            last_name = validated_data["last_name"]

        except:
            last_name = ""
        user = UserAccount(
            username=validated_data["username"],
            first_name=first_name,
            last_name=last_name,
            is_active=validated_data.get("is_active", True),
            is_staff=validated_data.get("is_staff", False),
            department_id=validated_data.get("department_id"),
            role_id=validated_data.get("role_id"),
        )
        user.set_password(validated_data["password"])  # Đặt mật khẩu
        user.save()
        return user
