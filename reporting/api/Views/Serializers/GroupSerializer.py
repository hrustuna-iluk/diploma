from reporting.models import Group, Teacher, Department
from rest_framework import serializers
from reporting.api.Views.Serializers.TeacherSerializer import TeacherSerializer
from reporting.api.Views.Serializers.DepartmentSerializer import DepartmentSerializer


class GroupSerializer(serializers.ModelSerializer):
    curator = TeacherSerializer()
    department = DepartmentSerializer()

    def create(self, validated_data):
        curator = validated_data.pop('curator')
        department = validated_data.pop('department')
        curator = Teacher.objects.get(**curator)
        department = Department.objects.get(**department)
        group = Group.objects.create(curator=curator, department=department, **validated_data)
        group.save()
        return group

    def update(self, group, validated_data):
        curator = Teacher.objects.get(**validated_data.get('curator'))
        department = Department.objects.get(**validated_data.get('department'))
        group.curator = curator
        group.department = department
        group.number = validated_data.get('number')
        group.leader = validated_data.get('leader')
        group.yearStudy = validated_data.get('yearStudy')
        group.tuition = validated_data.get('tuition')
        group.save()
        return group

    class Meta:
        model = Group
