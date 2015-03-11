from reporting.models import Group
from rest_framework import serializers
from reporting.api.Views.Serializers.TeacherSerializer import TeacherSerializer
from reporting.api.Views.Serializers.DepartmentSerializer import DepartmentSerializer


class GroupSerializer(serializers.ModelSerializer):
    curator = TeacherSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Group
