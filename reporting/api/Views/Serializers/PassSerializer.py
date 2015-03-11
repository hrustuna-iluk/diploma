from reporting.models import Pass
from rest_framework import serializers
from reporting.api.Views.Serializers.StudentSerializer import StudentSerializer


class PassSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:
        model = Pass
