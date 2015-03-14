from reporting.models import Report, Event
from rest_framework import serializers
from reporting.api.Views.Serializers.EventSerializer import EventSerializer


class ReportSerializer(serializers.ModelSerializer):
    event = EventSerializer()

    def create(self, validated_data):
        event = validated_data.pop('event')
        event = Event.objects.get(**event)
        report = Report.objects.create(event=event, **validated_data)
        report.save()
        return report

    def update(self, report, validated_data):
        event = Event.objects.get(**validated_data.get('event'))
        report.event = event
        report.date = validated_data.get('date')
        report.save()
        return report


    class Meta:
        model = Report
