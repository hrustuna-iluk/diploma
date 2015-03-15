from reporting.models import Faculty
from rest_framework import serializers


class FacultySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Faculty
