from reporting.models import Additional, Student
from rest_framework import serializers
from reporting.api.Views.Serializers.StudentSerializer import StudentSerializer

class AdditionalSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    def create(self, validated_data):
        student = validated_data.pop('student')
        student = Student.objects.get(**student)
        additional = Additional.objects.create(student=student, **validated_data)
        additional.save()
        return additional

    def update(self, additional, validated_data):
        title = validated_data.get('title')
        value = validated_data.get('value')
        student = Student.objects.get(**validated_data.get('student'))
        additional.title = title
        additional.value = value
        additional.student = student
        additional.save()
        return additional

    class Meta:
        model = Additional