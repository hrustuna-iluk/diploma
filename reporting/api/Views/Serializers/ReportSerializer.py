from reporting.models import Report, Event
from rest_framework import serializers
from reporting.api.Views.Serializers.EventSerializer import EventSerializer


class ReportSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    event = EventSerializer()

    def create(self, validated_data):
        event = validated_data.pop('event').get('id')
        event = Event.objects.get(pk=event)
        report = Report.objects.create(event=event, **validated_data)
        report.save()
        return report

    def update(self, report, validated_data):
        event = Event.objects.get(pk=validated_data.get('event').get('id'))
        report.event = event
        report.date = validated_data.get('date')
        report.save()
        return report


    class Meta:
        model = Report
