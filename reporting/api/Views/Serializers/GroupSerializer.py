from reporting.models import Group, Teacher, Department
from rest_framework import serializers
from reporting.api.Views.Serializers.TeacherSerializer import TeacherSerializer
from reporting.api.Views.Serializers.DepartmentSerializer import DepartmentSerializer


class GroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    curator = TeacherSerializer()
    department = DepartmentSerializer()

    def create(self, validated_data):
        department = validated_data.pop('department').get('id')
        department = Department.objects.get(pk=department)
        group = Group.objects.create(department=department, **validated_data)
        group.save()
        return group

    def update(self, group, validated_data):
        curator = Teacher.objects.get(pk=validated_data.get('curator').get('id'))

        department = Department.objects.get(pk=validated_data.get('department').get('id'))
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
