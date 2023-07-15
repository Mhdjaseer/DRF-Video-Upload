from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import vedio
from .models import Vedios

class vedioUploadView(viewsets.ViewSet):
    serializer_class = vedio

    def list(self, request):
        queryset = Vedios.objects.all()
        serializer = self.serializer_class(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
