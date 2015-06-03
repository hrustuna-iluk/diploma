from reporting.models import Faculty
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404, HttpResponse
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.FacultySerializer import FacultySerializer
from django.core.serializers import serialize


class FacultyView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None,  format=None):
        snippet = Faculty.objects.all()

        return HttpResponse(serialize('json', snippet, relations=('dean', )), content_type='application/json')

    def post(self, request, format=None):
        data = request.data
        if isinstance(data['dean'], dict):
            data['dean'] = data['dean']['id']
        serializer = FacultySerializer(data=request.data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance], relations=('dean', )), content_type='application/json', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = request.data
        if isinstance(data['dean'], dict):
            data['dean'] = data['dean']['id']
        snippet = get_object_or_404(Faculty, pk=request.data["id"])
        serializer = FacultySerializer(snippet, data=request.data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance], relations=('dean', )), content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Faculty, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)