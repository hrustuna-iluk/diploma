from reporting.models import PublicPlan
from rest_framework import serializers
from reporting.api.Views.Serializers.EventSerializer import EventSerializer
from reporting.api.Views.Serializers.TeacherSerializer import TeacherSerializer


class PublicPlanSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    responsive = TeacherSerializer(read_only=True)
    class Meta:
        model = PublicPlan
