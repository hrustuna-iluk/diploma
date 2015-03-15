from reporting.models import StudentWork
from rest_framework import serializers


class StudentWorkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        student_work = StudentWork.objects.create(**validated_data)
        student_work.save()
        return student_work

    def update(self, student_work, validated_data):
        student_work.group = validated_data.get('group')
        student_work.text = validated_data.get('text')
        student_work.year = validated_data.get('year')
        student_work.save()
        return student_work

    class Meta:
        model = StudentWork
