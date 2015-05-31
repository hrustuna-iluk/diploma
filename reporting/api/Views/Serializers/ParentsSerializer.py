from reporting.models import Parents
from rest_framework import serializers


class ParentsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        parent = Parents.objects.create(**validated_data)
        parent.save()
        return parent

    def update(self, parent, validated_data):
        parent.student = validated_data.get('student')
        parent.fullname = validated_data.get('fullname')
        parent.phone = validated_data.get('phone')
        parent.position = validated_data.get('position')
        parent.save()
        return parent

    class Meta:
        model = Parents
