from reporting.models import PublicPlan
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import Http404, HttpResponse
from django.template.context import RequestContext
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from reporting.api.Views.Serializers.PublicPlanSerializer import PublicPlanSerializer
from django.core.serializers import serialize


class PublicPlanView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk=None,  format=None):
        if pk:
            snippet = get_object_or_404(PublicPlan, pk=pk)
        else:
            snippet = PublicPlan.objects.all()

        return HttpResponse(serialize('json', snippet, relations=('event', 'responsive')), content_type='application/json')

    def post(self, request, format=None):
        data = request.data
        data['responsive'] = data['responsive']['id']
        serializer = PublicPlanSerializer(data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = request.data
        data['responsive'] = data['responsive']['id']
        snippet = get_object_or_404(PublicPlan, pk=request.data["id"])
        serializer = PublicPlanSerializer(snippet, data=data, context=RequestContext(request))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(PublicPlan, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)