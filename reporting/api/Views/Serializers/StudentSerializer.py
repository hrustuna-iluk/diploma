from reporting.models import Student, Benefits, Group, Language
from rest_framework import serializers
from reporting.api.Views.Serializers.LanguageSerializer import LanguageSerializer
from reporting.api.Views.Serializers.GroupSerializer import GroupSerializer
from reporting.api.Views.Serializers.BenefitsSerializer import BenefitsSerializer


class StudentSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    group = GroupSerializer()
    benefits = BenefitsSerializer(many=True)

    class Meta:
        model = Student

    def create(self, validated_data):
        language = validated_data.pop("language")
        group = validated_data.pop("group")
        benefits = [benefit["type"] for benefit in validated_data.pop("benefits")]

        language = Language.objects.get(**language)
        group = Group.objects.get(**group)
        benefits = Benefits.objects.filter(type__in=benefits)

        student = Student.objects.create(group=group, language=language, **validated_data)
        for benefit in benefits:
            student.benefits.add(benefit)
        student.save()
        return student

    def update(self, student, validated_data):
        language = validated_data.get("language")
        group = validated_data.get("group")
        benefits = [benefit["type"] for benefit in validated_data.get("benefits")]

        language = Language.objects.get(**language)
        group = Group.objects.get(**group)
        benefits = Benefits.objects.filter(type__in=benefits)

        student.firstName = validated_data.get("firstName")
        student.lastName = validated_data.get("lastName")
        student.middleName = validated_data.get("middleName")
        student.address = validated_data.get("address")
        student.phone = validated_data.get("phone")
        student.isProcurement = validated_data.get("isProcurement")
        student.dateBirth = validated_data.get("dateBirth")
        student.nationality = validated_data.get("nationality")
        student.maritalStatus = validated_data.get("maritalStatus")
        student.sex = validated_data.get("sex")
        student.school = validated_data.get("school")
        student.group = group
        student.language = language
        student.benefits.clear()
        for benefit in benefits:
            student.benefits.add(benefit)
        student.save()
        return student
