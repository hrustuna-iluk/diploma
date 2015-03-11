from reporting.models import Benefits
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.BenefitsSerializer import BenefitsSerializer


class BenefitsView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk=None,  format=None):
        if pk:
            snippet = get_object_or_404(Benefits, pk=pk)
            serializer = BenefitsSerializer(snippet, context=RequestContext(request))
        else:
            snippet = Benefits.objects.all()
            serializer = BenefitsSerializer(snippet, many=True, context=RequestContext(request))

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BenefitsSerializer(data=request.data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        snippet = get_object_or_404(Benefits, pk=request.data["id"])
        serializer = BenefitsSerializer(snippet, data=request.data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Benefits, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)