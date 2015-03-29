from reporting.models import Teacher
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404, HttpResponse
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.TeacherSerializer import TeacherSerializer
from django.core.serializers import serialize


class TeacherView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk=None,  format=None):
        if pk:
            snippet = Teacher.objects.filter(department__id=pk)
        else:
            snippet = Teacher.objects.all()

        return HttpResponse(serialize('json', snippet, relations=('department', )), content_type='application/json')

    def post(self, request, format=None):
        data = request.data
        if isinstance(data['department'], dict):
            data['department'] = data['department']["id"]

            if data['position'] != 'teacher':
                teacher = Teacher.objects.get(department=data['department'], position=data['position'])
                if teacher:
                    teacher.position = 'teacher'
                    teacher.save()
        serializer = TeacherSerializer(data=data, context=RequestContext(request))

        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [serializer.instance], relations=('department', )), content_type='application/json', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = request.data
        if isinstance(data['department'], dict):
            data['department'] = data['department']["id"]

            if data['position'] != 'teacher':
                teacher = Teacher.objects.get(department=data['department'], position=data['position'])
                if teacher:
                    teacher.position = 'teacher'
                    teacher.save()

        snippet = get_object_or_404(Teacher, pk=request.data["id"])
        serializer = TeacherSerializer(snippet, data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serialize('json', [snippet], relations=('department', )), content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Teacher, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)