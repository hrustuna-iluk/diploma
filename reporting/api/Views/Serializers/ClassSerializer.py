from reporting.models import Class
from rest_framework import serializers


class ClassSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        class_instance = Class.objects.create(**validated_data)
        class_instance.save()
        return class_instance

    def update(self, class_instance, validated_data):
        class_instance.teacher = validated_data.get('teacher')
        class_instance.group = validated_data.get('group')
        class_instance.subject = validated_data.get('subject')
        class_instance.classRoom = validated_data.get('classRoom')
        class_instance.day = validated_data.get('day')
        class_instance.number_of_week = validated_data.get('number_of_week')
        class_instance.semester = validated_data.get('semester')
        class_instance.number = validated_data.get('number')
        class_instance.save()
        return class_instance

    class Meta:
        model = Class
