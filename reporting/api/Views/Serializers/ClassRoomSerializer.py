from reporting.models import ClassRoom
from rest_framework import serializers


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
