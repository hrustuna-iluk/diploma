from reporting.models import PublicPlan, Teacher, Event
from rest_framework import serializers
from reporting.api.Views.Serializers.EventSerializer import EventSerializer
from reporting.api.Views.Serializers.TeacherSerializer import TeacherSerializer


class PublicPlanSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    event = EventSerializer()
    responsive = TeacherSerializer()

    def create(self, validated_data):
        teacher = validated_data.pop('teacher').get('id')
        event = validated_data.pop('event').get('id')
        teacher = Teacher.objects.get(pk=teacher)
        event = Event.objects.get(pk=event)
        public_plan = PublicPlan.objects.create(teacher=teacher, event=event, **validated_data)
        public_plan.save()
        return public_plan

    def update(self, public_plan, validated_data):
        teacher = Teacher.objects.get(pk=validated_data.get('teacher').get('id'))
        event = Event.objects.get(pk=validated_data.get('event').get('id'))
        public_plan.teacher = teacher
        public_plan.event = event
        public_plan.date = validated_data.get('date')
        public_plan.description = validated_data.get('description')
        public_plan.amount_hours = validated_data.get('amount_hours')
        public_plan.amount_present = validated_data.get('amount_present')
        public_plan.save()
        return public_plan

    class Meta:
        model = PublicPlan
