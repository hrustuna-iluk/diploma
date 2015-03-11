from reporting.models import Faculty
from rest_framework import serializers


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
