from reporting.models import Teacher
from rest_framework import serializers
from reporting.api.Views.Serializers.DepartmentSerializer import DepartmentSerializer


class TeacherSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Teacher
