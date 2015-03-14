from reporting.models import Pass, Student, Class
from rest_framework import serializers
from reporting.api.Views.Serializers.StudentSerializer import StudentSerializer
from reporting.api.Views.Serializers.ClassSerializer import ClassSerializer

class PassSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class_passed = ClassSerializer()

    def create(self, validated_data):
        student = validated_data.pop('student')
        student = Student.objects.get(**student)
        pass_instance = Pass.objects.create(student=student, **validated_data)
        pass_instance.save()
        return pass_instance

    def update(self, pass_instance, validated_data):
        student = Student.objects.get(**validated_data.pop('student'))
        class_passed = Class.objects.get(**validated_data.pop('class_passed'))
        pass_instance.student = student
        pass_instance.date = validated_data.pop('date')
        pass_instance.type = validated_data.pop('type')
        pass_instance.class_passed = class_passed
        pass_instance.save()
        return pass_instance

    class Meta:
        model = Pass
