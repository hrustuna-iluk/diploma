from reporting.models import Benefits
from rest_framework import serializers


class BenefitsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Benefits
