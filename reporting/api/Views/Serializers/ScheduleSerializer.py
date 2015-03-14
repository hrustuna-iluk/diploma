from reporting.models import Schedule, Group
from rest_framework import serializers
from reporting.api.Views.Serializers.GroupSerializer import GroupSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    def create(self, validated_data):
        group = validated_data.pop('group')
        schedule = Schedule.objects.create(group=group)
        schedule.save()
        return schedule

    def update(self, schedule, validated_data):
        group = Group.objects.get(**validated_data.get('group'))
        schedule.group = group
        schedule.save()
        return schedule

    class Meta:
        model = Schedule
