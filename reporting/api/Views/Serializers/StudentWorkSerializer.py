from reporting.models import StudentWork, Group
from rest_framework import serializers
from reporting.api.Views.Serializers.GroupSerializer import GroupSerializer


class StudentWorkSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    def create(self, validated_data):
        group = validated_data.pop('group')
        group = Group.objects.get(**group)
        student_work = StudentWork.objects.create(group=group, **validated_data)
        student_work.save()
        return student_work

    def update(self, student_work, validated_data):
        group = validated_data.get('group')
        group = Group.objects.get(**group)
        student_work.group = group
        student_work.text = validated_data.get('text')
        student_work.year = validated_data.get('year')
        student_work.save()
        return student_work

    class Meta:
        model = StudentWork
