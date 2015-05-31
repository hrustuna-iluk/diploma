from reporting.models import Language
from rest_framework import serializers


class LanguageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Language
