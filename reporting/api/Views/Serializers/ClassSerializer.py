from reporting.models import Class, Teacher, Schedule
from rest_framework import serializers
from reporting.api.Views.Serializers.TeacherSerializer import TeacherSerializer
from reporting.api.Views.Serializers.ScheduleSerializer import ScheduleSerializer


class ClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    schedule = ScheduleSerializer()

    def create(self, validated_data):
        teacher = validated_data.pop('teacher')
        schedule = validated_data.pop('schedule')
        class_instance = Class.objects.create(teacher=teacher, schedule=schedule, **validated_data)
        class_instance.save()
        return class_instance

    def update(self, class_instance, validated_data):
        teacher = Teacher.objects.get(validated_data.get('teacher'))
        schedule = Schedule.objects.get(validated_data.get('schedule'))
        class_instance.teacher = teacher
        class_instance.schedule = schedule
        class_instance.subject = validated_data.get('subject')
        class_instance.classRoom = validated_data.get('classRoom')
        class_instance.day = validated_data.get('day')
        class_instance.number_of_week = validated_data.get('number_of_week')
        class_instance.number = validated_data.get('number')
        class_instance.save()
        return class_instance

    class Meta:
        model = Class
