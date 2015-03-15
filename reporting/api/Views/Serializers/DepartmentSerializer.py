from reporting.models import Department, Teacher
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        teacher = validated_data.pop('headOfDepartment')
        if teacher:
            teacher = Teacher.objects.get(pk=teacher.get('id'))
            department = Department.objects.create(headOfDepartment=teacher, **validated_data)
        else:
            department = Department.objects.create(**validated_data)
        department.save()
        return department

    def update(self, department, validated_data):
        headOfDepartment = validated_data.get('headOfDepartment').get('id')
        headOfDepartment = Teacher.objects.get(pk=headOfDepartment)
        department.headOfDepartment = headOfDepartment
        department.title = validated_data.get('title')
        department.save()
        return department


    class Meta:
        model = Department
