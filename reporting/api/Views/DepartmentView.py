from reporting.models import Department
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.DepartmentSerializer import DepartmentSerializer
from django.core.serializers import serialize
from django.http import HttpResponse


class DepartmentView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk=None,  format=None):
        snippet = Department.objects.all()

        return HttpResponse(serialize('json', snippet, relations=('headOfDepartment', )), content_type="application/json")

    def post(self, request, format=None):
        data = request.data
        if isinstance(data['headOfDepartment'], dict):
            data['headOfDepartment'] = data['headOfDepartment']['id']
        if isinstance(data['faculty'], dict):
            data['faculty'] = data['faculty']['id']
        serializer = DepartmentSerializer(data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance], relations=('headOfDepartment', )), content_type="application/json", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = request.data
        if isinstance(data['headOfDepartment'], dict):
            data['headOfDepartment'] = data['headOfDepartment']['id']
        if isinstance(data['faculty'], dict):
            data['faculty'] = data['faculty']['id']
        snippet = get_object_or_404(Department, pk=request.data["id"])
        serializer = DepartmentSerializer(snippet, data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [snippet], relations=('headOfDepartment', )), content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Department, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)