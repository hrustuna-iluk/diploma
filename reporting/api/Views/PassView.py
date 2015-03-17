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
            snippet = get_object_or_404(Pass, pk=pk)
        else:
            snippet = Pass.objects.all()

        return HttpResponse(serialize('json', snippet, relations=('student', 'class_passed')), content_type='application/json')

    def post(self, request, format=None):
        serializer = PassSerializer(data=request.data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        snippet = get_object_or_404(Pass, pk=request.data["id"])
        serializer = PassSerializer(snippet, data=request.data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Pass, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)