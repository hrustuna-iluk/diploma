from reporting.models import StudentWork
from rest_framework import serializers
from reporting.api.Views.Serializers.GroupSerializer import GroupSerializer


class StudentWorkSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    class Meta:
        model = StudentWork
