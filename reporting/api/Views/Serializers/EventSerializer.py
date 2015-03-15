from reporting.models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Event
