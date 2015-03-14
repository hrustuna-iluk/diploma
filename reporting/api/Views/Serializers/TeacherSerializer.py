from reporting.models import Teacher, Department
from rest_framework import serializers
from reporting.api.Views.Serializers.DepartmentSerializer import DepartmentSerializer


class TeacherSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    def create(self, validated_data):
        department = validated_data.pop('department')
        department = Department.objects.get(**department)
        teacher = Teacher.objects.create(department=department, **validated_data)
        teacher.save()
        return teacher

    def update(self, teacher, validated_data):
        department = Department.objects.get(**validated_data.get('department'))
        teacher.department = department
        teacher.firstName = validated_data.get('firstName')
        teacher.lastName = validated_data.get('lastName')
        teacher.middleName = validated_data.get('middleName')
        teacher.position = validated_data.get('position')
        teacher.save()
        return teacher

    class Meta:
        model = Teacher
