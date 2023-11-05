from rest_framework import serializers

from .models import *


class TypeOfDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfDepartmentModel
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    typeOfDepartment_id = TypeOfDepartmentSerializer()

    class Meta:
        model = DepartmentModel
        fields = (
            "id",
            "department_name",
            "department_code",
            "isCenterDepartment",
            "typeOfDepartment_id",
        )


class RoomDepartmentSerializer(serializers.ModelSerializer):
    department_id = DepartmentSerializer()

    class Meta:
        model = RoomDepartmentModel
        fields = ("id", "roomDepartment_code", "roomDepartment_name", "department_id")
