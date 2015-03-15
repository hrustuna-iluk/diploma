from reporting.models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Student

    def create(self, validated_data):
        benefits = validated_data.pop('benefits')
        student = Student.objects.create(**validated_data)
        for benefit in benefits:
            student.benefits.add(benefit)
        student.save()
        return student

    def update(self, student, validated_data):
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
        student.group = validated_data.get("group")
        student.language = validated_data.get("language")
        student.benefits.clear()
        for benefit in validated_data.get("benefits"):
            student.benefits.add(benefit)
        student.save()
        return student
