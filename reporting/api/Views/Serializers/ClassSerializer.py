from reporting.models import Class
from rest_framework import serializers
from reporting.api.Views.Serializers.SubjectSerializer import SubjectSerializer
from reporting.api.Views.Serializers.TeacherSerializer import TeacherSerializer
from reporting.api.Views.Serializers.ClassRoomSerializer import ClassRoomSerializer


class ClassSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    classRoom = ClassRoomSerializer(read_only=True)
    class Meta:
        model = Class
