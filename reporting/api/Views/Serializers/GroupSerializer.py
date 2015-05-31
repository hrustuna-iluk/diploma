from reporting.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        editorialBoards = validated_data.pop('editorialBoard')
        otherTasks = validated_data.pop('otherTasks')
        group = Group.objects.create(**validated_data)
        for editorialBoard in editorialBoards:
            group.editorialBoard.add(editorialBoard)
        for otherTask in otherTasks:
            group.otherTasks.add(otherTask)
        group.save()
        return group

    def update(self, group, validated_data):
        group.curator = validated_data.get('curator')
        group.department = validated_data.get('department')
        group.number = validated_data.get('number')
        group.leader = validated_data.get('leader')
        group.yearStudy = validated_data.get('yearStudy')
        group.tuition = validated_data.get('tuition')
        group.leader = validated_data.get('leader')
        group.deputyHeadman = validated_data.get('deputyHeadman')
        group.organizer = validated_data.get('organizer')
        group.culturalWork = validated_data.get('culturalWork')
        group.healthWork = validated_data.get('healthWork')
        group.editorialBoard.clear()
        group.otherTasks.clear()
        for editorialBoard in validated_data.get('editorialBoard'):
            group.editorialBoard.add(editorialBoard)
        for otherTask in validated_data.get('otherTasks'):
            group.otherTasks.add(otherTask)
        group.save()
        return group

    class Meta:
        model = Group
