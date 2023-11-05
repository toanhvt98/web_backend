from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password
from departments.serializers import RoomDepartmentSerializer


class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
        )

    def validate(self, attrs):
        user = UserAccount(**attrs)
        password = user.password
        validate_password(password, user)
        return attrs

    def create(self, validated_data):
        user = UserAccount(
            username=validated_data.get("username"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            is_active=validated_data.get("is_active", True),
            is_staff=validated_data.get("is_staff", False),
        )
        user.set_password(validated_data.get("password"))  # Đặt mật khẩu
        user.save()
        return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "is_active",
            "is_superuser",
            "is_staff",
        )


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = "__all__"


class RoomDepartmentRoleUserSerializer(serializers.ModelSerializer):
    user_id = AccountSerializer()
    role_id = RoleSerializer()
    roomDepartment_id = RoomDepartmentSerializer()

    class Meta:
        model = RoomDepartmentRoleUserModel
        fields = "__all__"
