from reporting.models import Pass, Student, Class
from rest_framework import serializers
from reporting.api.Views.Serializers.StudentSerializer import StudentSerializer
from reporting.api.Views.Serializers.ClassSerializer import ClassSerializer

class PassSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        pass_instance = Pass.objects.create(**validated_data)
        pass_instance.save()
        return pass_instance

    def update(self, pass_instance, validated_data):
        pass_instance.student = validated_data.pop('student')
        pass_instance.date = validated_data.pop('date')
        pass_instance.type = validated_data.pop('type')
        pass_instance.class_passed = validated_data.pop('class_passed')
        pass_instance.save()
        return pass_instance

    class Meta:
        model = Pass
