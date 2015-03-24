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
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk=None,  format=None):
        if pk:
            snippet = get_object_or_404(Group, pk=pk)
        else:
            snippet = Group.objects.all()

        return HttpResponse(serialize('json', snippet, relations=(
            'department', 'leader', 'deputyHeadman', 'organizer',
            'culturalWork', 'healthWork', 'editorialBoard', 'otherTasks', 'curator'
        )), content_type='application/json')

    def post(self, request, format=None):
        data = request.data
        if data['department']:
            data['department'] = data['department'].get('id')
        if data['leader']:
            data['leader'] = data['leader'].get('id')
        if data['deputyHeadman']:
            data['deputyHeadman'] = data['deputyHeadman'].get('id')
        if data['organizer']:
            data['organizer'] = data['organizer'].get('id')
        if data['culturalWork']:
            data['culturalWork'] = data['culturalWork'].get('id')
        if data['healthWork']:
            data['healthWork'] = data['healthWork'].get('id')
        if data['editorialBoard']:
            data['editorialBoard'] = [item.get('id') for item in data['editorialBoard']]
        if data['otherTasks']:
            data['otherTasks'] = [item.get('id') for item in data['otherTasks']]
        if data['curator']:
            data['curator'] = data['curator'].get('id')
        serializer = GroupSerializer(data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = request.data
        snippet = get_object_or_404(Group, pk=request.data["id"])
        serializer = GroupSerializer(snippet, data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Group, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)