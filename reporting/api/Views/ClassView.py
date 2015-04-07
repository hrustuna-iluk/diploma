from reporting.models import Class
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404, HttpResponse
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.ClassSerializer import ClassSerializer
from django.core.serializers import serialize


class ClassView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk=None,  format=None):
        if request.GET.get('group'):
            snippet = Class.objects.filter(group__id=request.GET.get('group'))
        else:
            snippet = Class.objects.all()

        return HttpResponse(serialize('json', snippet, relations=('teacher', 'group')), content_type='application/json')

    def post(self, request, format=None):
        data = request.data
        if isinstance(data['teacher'], dict):
            data['teacher'] = data['teacher']['id']
        if isinstance(data['group'], dict):
            data['group'] = data['group']['id']
        serializer = ClassSerializer(data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance], relations=('teacher', 'group')),
                                status=status.HTTP_201_CREATED, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = request.data
        if isinstance(data['teacher'], dict):
            data['teacher'] = data['teacher']['id']
        if isinstance(data['group'], dict):
            data['group'] = data['group']['id']
        snippet = get_object_or_404(Class, pk=request.data["id"])
        serializer = ClassSerializer(snippet, data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [snippet], relations=('teacher', 'group')),
                                content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Class, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)