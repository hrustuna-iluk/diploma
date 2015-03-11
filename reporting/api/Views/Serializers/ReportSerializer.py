from reporting.models import Report
from rest_framework import serializers
from reporting.api.Views.Serializers.EventSerializer import EventSerializer


class ReportSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    class Meta:
        model = Report
