from reporting.models import Student
from rest_framework import serializers
from reporting.api.Views.Serializers.LanguageSerializer import LanguageSerializer
from reporting.api.Views.Serializers.GroupSerializer import GroupSerializer


class StudentSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Student
