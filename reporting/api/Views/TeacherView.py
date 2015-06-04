from reporting.models import Teacher
from reporting.manage_users import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404, HttpResponse
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.TeacherSerializer import TeacherSerializer
from django.core.serializers import serialize
from reporting.manage_users import *


class TeacherView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None,  format=None):
        if request.GET.get('department'):
            snippet = Teacher.objects.filter(department__id=request.GET.get('department'))
        else:
            snippet = Teacher.objects.all()

        return HttpResponse(serialize('json', snippet, relations=('department', 'user')), content_type='application/json')

    def post(self, request, format=None):
        data = request.data
        if isinstance(data['department'], dict):
            data['department'] = data['department']["id"]

        if data['position'] != 'teacher':
            try:
                teacher = None
                if data['position'] == 'Deputy Dean' or data['position'] == 'dean':
                    teacher = Teacher.objects.get(position=data['position'])
                elif data['position'] == 'Head of Department':
                    teacher = Teacher.objects.get(department=data['department'], position=data['position'])
                teacher.position = 'teacher'
                teacher.save()
            except Teacher.DoesNotExist:
                pass
        serializer = TeacherSerializer(data=data, context=RequestContext(request))

        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance], relations=('department', 'user')), content_type='application/json', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        data = request.data
        if isinstance(data['department'], dict):
            data['department'] = data['department']["id"]

        try:
            teacher = get_object_or_404(Teacher, pk=request.data["id"])
            teacher.position = 'teacher'
            if data['user'] and isinstance(data['user'], dict):
                if not teacher.user:
                    user = create_user({
                        'username': data['user']['username'],
                        'password': data['user']['password'],
                        'email': teacher.email
                    })
                    add_permission(user, data['position'])
                    teacher.user = user
                    data['user'] = user.id
                else:
                    user = User.objects.get(id=data['user']['id'])
                    user.username = data['user']['username']
                    user.set_password(data['user']['password'])
                    user.is_active = data['user']['is_active']
                    user.save()
                    data['user'] = user.id
                teacher.save()
        except Teacher.DoesNotExist:
            pass
        snippet = get_object_or_404(Teacher, pk=request.data["id"])
        serializer = TeacherSerializer(snippet, data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance], relations=('department', 'user')), content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Teacher, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)