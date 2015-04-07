from reporting.models import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        department = Department.objects.create(**validated_data)
        department.save()
        return department

    def update(self, department, validated_data):
        department.headOfDepartment = validated_data.get('headOfDepartment')
        department.title = validated_data.get('title')
        department.specialization = validated_data.get('specialization')
        department.save()
        return department


    class Meta:
        model = Department
