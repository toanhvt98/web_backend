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
        fields = ('id', 'roomDepartment_name','department_id',)

    def get_fields(self):
        fields = super(RoomDepartmentSerializer, self).get_fields()
        request = self.context.get('request')
        if request and request.method == 'GET':
            fields['department_id'] = DepartmentSerializer()
        return fields
