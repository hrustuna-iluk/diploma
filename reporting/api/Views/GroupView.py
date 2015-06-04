from reporting.models import Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404, HttpResponse
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.GroupSerializer import GroupSerializer
from django.core.serializers import serialize


class GroupView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None,  format=None):
        if request.GET.get('department'):
            snippet = Group.objects.filter(department__id=request.GET.get('department'))
        else:
            snippet = Group.objects.all()

        return HttpResponse(serialize('json', snippet, relations=(
            'department', 'leader', 'deputyHeadman', 'organizer',
            'culturalWork', 'healthWork', 'editorialBoard', 'otherTasks', 'curator'
        )), content_type='application/json')

    def post(self, request, format=None):
        data = request.data
        if isinstance(data['department'], dict):
            data['department'] = data['department']['id']
        if isinstance(data['leader'], dict):
            data['leader'] = data['leader']['id']
        if isinstance(data['deputyHeadman'], dict):
            data['deputyHeadman'] = data['deputyHeadman']['id']
        if isinstance(data['organizer'], dict):
            data['organizer'] = data['organizer']['id']
        if isinstance(data['culturalWork'], dict):
            data['culturalWork'] = data['culturalWork']['id']
        if isinstance(data['healthWork'], dict):
            data['healthWork'] = data['healthWork']['id']
        if isinstance(data['curator'], dict):
            data['curator'] = data['curator']['id']
        serializer = GroupSerializer(data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance], relations=(
            'department', 'leader', 'deputyHeadman', 'organizer',
            'culturalWork', 'healthWork', 'editorialBoard', 'otherTasks', 'curator'
        )), content_type='application/json', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        data = request.data
        if isinstance(data['department'], dict):
            data['department'] = data['department']['id']
        if isinstance(data['leader'], dict):
            data['leader'] = data['leader']['id']
        if isinstance(data['deputyHeadman'], dict):
            data['deputyHeadman'] = data['deputyHeadman']['id']
        if isinstance(data['organizer'], dict):
            data['organizer'] = data['organizer']['id']
        if isinstance(data['culturalWork'], dict):
            data['culturalWork'] = data['culturalWork']['id']
        if isinstance(data['healthWork'], dict):
            data['healthWork'] = data['healthWork']['id']
        if isinstance(data['editorialBoard'], dict):
            data['editorialBoard'] = [item['id'] for item in data['editorialBoard'] if isinstance(item, dict)]
        if isinstance(data['otherTasks'], dict):
            data['otherTasks'] = [item['id'] for item in data['otherTasks'] if isinstance(item, dict)]
        if isinstance(data['curator'], dict):
            data['curator'] = data['curator']['id']
        snippet = get_object_or_404(Group, pk=request.data["id"])
        serializer = GroupSerializer(snippet, data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [snippet], relations=(
            'department', 'leader', 'deputyHeadman', 'organizer',
            'culturalWork', 'healthWork', 'editorialBoard', 'otherTasks', 'curator'
        )), content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Group, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)