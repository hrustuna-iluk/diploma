from reporting.models import Class, Teacher, Group, Department
from rest_framework import serializers
from reporting.api.Views.Serializers.TeacherSerializer import TeacherSerializer
from reporting.api.Views.Serializers.GroupSerializer import GroupSerializer


class ClassSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    teacher = TeacherSerializer()
    group = GroupSerializer()

    def create(self, validated_data):
        teacher = validated_data.pop('teacher').get('id')
        group = validated_data.pop('group').get('id')
        teacher = Teacher.objects.get(pk=teacher)
        group = Group.objects.get(pk=group)
        class_instance = Class.objects.create(teacher=teacher, group=group, **validated_data)
        class_instance.save()
        return class_instance

    def update(self, class_instance, validated_data):
        teacher = Teacher.objects.get(pk=validated_data.get('teacher').get('id'))
        group = Group.objects.get(pk=validated_data.get('group').get('id'))
        class_instance.teacher = teacher
        class_instance.group = group
        class_instance.subject = validated_data.get('subject')
        class_instance.classRoom = validated_data.get('classRoom')
        class_instance.day = validated_data.get('day')
        class_instance.number_of_week = validated_data.get('number_of_week')
        class_instance.number = validated_data.get('number')
        class_instance.save()
        return class_instance

    class Meta:
        model = Class
        exclude = ('teacher', 'group')
