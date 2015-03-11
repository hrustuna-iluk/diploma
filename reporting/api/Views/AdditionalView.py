from reporting.models import Additional
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.AdditionalSerializer import AdditionalSerializer


class AdditionalView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk=None,  format=None):
        if pk:
            snippet = get_object_or_404(Additional, pk=pk)
            serializer = AdditionalSerializer(snippet, context=RequestContext(request))
        else:
            snippet = Additional.objects.all()
            serializer = AdditionalSerializer(snippet, many=True, context=RequestContext(request))

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdditionalSerializer(data=request.data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        snippet = get_object_or_404(Additional, pk=request.data["id"])
        serializer = AdditionalSerializer(snippet, data=request.data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Additional, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)