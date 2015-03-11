from reporting.models import Parents
from rest_framework import serializers
from reporting.api.Views.Serializers.StudentSerializer import StudentSerializer


class ParentsSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:
        model = Parents
