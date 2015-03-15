from reporting.models import Parents, Student
from rest_framework import serializers
from reporting.api.Views.Serializers.StudentSerializer import StudentSerializer


class ParentsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    student = StudentSerializer()

    def create(self, validated_data):
        student = validated_data.pop('student').get('id')
        student = Student.objects.get(pk=student)
        parent = Parents.objects.create(student=student, **validated_data)
        parent.save()
        return parent

    def update(self, parent, validated_data):
        student = Student.objects.get(pk=validated_data.get('student').get('id'))
        parent.student = student
        parent.fullname = validated_data.get('fullname')
        parent.phone = validated_data.get('phone')
        parent.position = validated_data.get('position')
        parent.save()
        return parent

    class Meta:
        model = Parents
