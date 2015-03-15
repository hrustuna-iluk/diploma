from reporting.models import Teacher, Department
from rest_framework import serializers
from reporting.api.Views.Serializers.DepartmentSerializer import DepartmentSerializer


class TeacherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    department = DepartmentSerializer()

    def create(self, validated_data):
        department = validated_data.pop('department').get('id')
        department = Department.objects.get(pk=department)
        teacher = Teacher.objects.create(department=department, **validated_data)
        teacher.save()
        return teacher

    def update(self, teacher, validated_data):
        department = Department.objects.get(pk=validated_data.get('department').get('id'))
        teacher.department = department
        teacher.firstName = validated_data.get('firstName')
        teacher.lastName = validated_data.get('lastName')
        teacher.middleName = validated_data.get('middleName')
        teacher.position = validated_data.get('position')
        teacher.save()
        return teacher

    class Meta:
        model = Teacher
