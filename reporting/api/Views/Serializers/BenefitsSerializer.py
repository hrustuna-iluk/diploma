from reporting.models import Benefits
from rest_framework import serializers


class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
