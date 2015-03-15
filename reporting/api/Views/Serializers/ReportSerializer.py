from reporting.models import Report
from rest_framework import serializers


class ReportSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        report = Report.objects.create(**validated_data)
        report.save()
        return report

    def update(self, report, validated_data):
        report.event = validated_data.get('event')
        report.date = validated_data.get('date')
        report.save()
        return report


    class Meta:
        model = Report
