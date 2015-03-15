from reporting.models import PublicPlan, Teacher, Event
from rest_framework import serializers


class PublicPlanSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        public_plan = PublicPlan.objects.create(**validated_data)
        public_plan.save()
        return public_plan

    def update(self, public_plan, validated_data):
        public_plan.teacher = validated_data.get('teacher')
        public_plan.event = validated_data.get('event')
        public_plan.date = validated_data.get('date')
        public_plan.description = validated_data.get('description')
        public_plan.amount_hours = validated_data.get('amount_hours')
        public_plan.amount_present = validated_data.get('amount_present')
        public_plan.save()
        return public_plan

    class Meta:
        model = PublicPlan
