from reporting.models import Benefits
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404, HttpResponse
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.BenefitsSerializer import BenefitsSerializer
from django.core.serializers import serialize


class BenefitsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None,  format=None):
        snippet = Benefits.objects.all()

        return HttpResponse(serialize('json', snippet), content_type='application/json')

    def post(self, request, format=None):
        serializer = BenefitsSerializer(data=request.data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance]), content_type='application/json', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        snippet = get_object_or_404(Benefits, pk=request.data["id"])
        serializer = BenefitsSerializer(snippet, data=request.data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [snippet]), content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Benefits, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)