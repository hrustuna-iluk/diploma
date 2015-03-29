from reporting.models import Pass
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404, HttpResponse
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.PassSerializer import PassSerializer
from django.core.serializers import serialize


class PassView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk=None,  format=None):
        if pk:
            snippet = Pass.objects.filter(student__id=pk)
        else:
            snippet = Pass.objects.all()

        return HttpResponse(serialize('json', snippet, relations=('student', 'class_passed')), content_type='application/json')

    def post(self, request, format=None):
        data = request.data
        serializer = PassSerializer(data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance], relations=('student', 'class_passed')), content_type='application/json', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = request.data
        if isinstance(data['class_passed'], dict):
            data['class_passed'] = data['class_passed']['id']
        if isinstance(data['student'], dict):
            data['student'] = data['student']['id']
        snippet = get_object_or_404(Pass, pk=request.data["id"])
        serializer = PassSerializer(snippet, data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [snippet], relations=('student', 'class_passed')), content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Pass, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)