from reporting.models import Teacher
from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        teacher = Teacher.objects.create(**validated_data)
        teacher.save()
        return teacher

    def update(self, teacher, validated_data):
        teacher.department = validated_data.get('department')
        teacher.firstName = validated_data.get('firstName')
        teacher.lastName = validated_data.get('lastName')
        teacher.middleName = validated_data.get('middleName')
        teacher.position = validated_data.get('position')
        teacher.save()
        return teacher

    class Meta:
        model = Teacher
