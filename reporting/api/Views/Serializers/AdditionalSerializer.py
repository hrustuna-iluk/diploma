from reporting.models import Additional
from rest_framework import serializers
from reporting.api.Views.Serializers.StudentSerializer import StudentSerializer

class AdditionalSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:
        model = Additional
