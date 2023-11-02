from rest_framework import serializers

from .models import *

class TypeOfDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfDepartmentModel
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        fields = '__all__'

class RoomDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomDepartmentModel
        fields = ('id', 'roomDepartment_name','department_id','typeOfDepartment_id')

