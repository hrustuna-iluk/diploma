from reporting.models import Student, Parents
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
            snippet = Student.objects.filter(group__id=pk)
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
        if isinstance(data['group'], dict):
            data['group'] = data['group']['id']
        father = Parents.objects.create(**data['father'])
        mother = Parents.objects.create(**data['mother'])
        father.save()
        mother.save()
        data['father'] = father.id
        data['mother'] = mother.id
        serializer = StudentSerializer(data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance], relations={
            'language': {},
            'benefits': {},
            'mother': {},
            'father': {},
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = request.data
        if isinstance(data['group'], dict):
            data['group'] = data['group']['id']
        snippet = get_object_or_404(Student, pk=request.data["id"])
        serializer = StudentSerializer(snippet, data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [snippet], relations={
            'language': {},
            'benefits': {},
            'mother': {},
            'father': {},
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Student, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)