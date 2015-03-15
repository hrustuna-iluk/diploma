from reporting.models import Additional
from rest_framework import serializers
from reporting.api.Views.Serializers.StudentSerializer import StudentSerializer

class AdditionalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        additional = Additional.objects.create(**validated_data)
        additional.save()
        return additional

    def update(self, additional, validated_data):
        additional.title = validated_data.get('title')
        additional.value = validated_data.get('value')
        additional.student = validated_data.get('student')
        additional.save()
        return additional

    class Meta:
        model = Additional