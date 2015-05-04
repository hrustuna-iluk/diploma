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
from reporting.manage_users import *


class StudentView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None,  format=None):
        if request.GET.get('group'):
            snippet = Student.objects.filter(group__id=request.GET['group'])
        elif request.GET.get('department'):
            snippet = Student.objects.filter(group__id=request.GET['department'])
        else:
            snippet = Student.objects.all()
        return HttpResponse(serialize('json', snippet, relations={
            'language': {},
            'benefits': {},
            'father': {},
            'mother': {},
            'user': {},
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
        if isinstance(data['language'], dict):
            data['language'] = data['language']['id']
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
                'user': {},
                'group': {
                    'relations': (
                        'department',
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
        if isinstance(data['language'], dict):
            data['language'] = data['language']['id']
        if isinstance(data['group'], dict):
            data['group'] = data['group']['id']
        if isinstance(data['mother'], dict):
            data['mother'] = data['mother']['id']
        if isinstance(data['father'], dict):
            data['father'] = data['father']['id']
        data['benefits'] = [item['id'] for item in data['benefits'] if isinstance(item, dict)]
        snippet = get_object_or_404(Student, pk=request.data["id"])
        if not snippet.user and snippet.group.leader.id == snippet.id:
            user = create_user({
                'username': data['user']['username'],
                'password': data['user']['password'],
                'email': snippet.email
            })
            add_permission(user, 'group_leader')
            snippet.user = user
            data['user'] = user.id
        elif data['user']:
            user = User.objects.get(id=data['user']['id'])
            user.username = data['user']['username']
            user.set_password(data['user']['password'])
            user.save()
            data['user'] = user.id
        serializer = StudentSerializer(snippet, data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance], relations={
                'language': {},
                'benefits': {},
                'mother': {},
                'father': {},
                'user': {},
                'group': {
                    'relations': (
                        'department',
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