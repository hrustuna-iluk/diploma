from reporting.models import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Department
