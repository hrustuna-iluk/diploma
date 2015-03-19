from reporting.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404, HttpResponse
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.StudentSerializer import StudentSerializer
from django.core.serializers import serialize


class StudentView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk=None,  format=None):
        if pk:
            snippet = get_object_or_404(Student, pk=pk)
        else:
            snippet = Student.objects.all()
        return HttpResponse(serialize('json', snippet, relations={
            'language': {},
            'benefits': {},
            'group': {
                'relations': ('department',
                              'editorialBoard',
                              'headOfDepartment',
                              'culturalWork',
                              'deputyHeadman',
                              'otherTasks',
                              'organizer',
                              'curator',
                              'leader'
                )
            }
        }), content_type='application/json')

    def post(self, request, format=None):
        data = request.data
        data['language'] = data['language']['id']
        data['benefits'] = [item['id'] for item in data['benefits']]
        data['group'] = data['group']['id']
        serializer = StudentSerializer(data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = request.data
        data['language'] = data['language']['id']
        data['benefits'] = [item['id'] for item in data['benefits']]
        data['group'] = data['group']['id']
        snippet = get_object_or_404(Student, pk=request.data["id"])
        serializer = StudentSerializer(snippet, data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Student, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)