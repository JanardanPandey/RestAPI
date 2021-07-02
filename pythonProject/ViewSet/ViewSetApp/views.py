from django.shortcuts import render
from .models import ITAssetsModel
from .serializers import ItAssetsSerializers
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets


class ItAssetsApi(viewsets.ViewSet):
    def list(self, request):
        stu = ITAssetsModel.objects.all()
        seializer = ItAssetsSerializers(stu, many=True)
        return  Response(seializer.data)
    def retrieve(self, request, pk):
        stu = ITAssetsModel.objects.get(id = pk)
        serializer = ItAssetsSerializers(stu)
        return Response(serializer.data)
    def create(self, request):
        stu = request.data
        serializer = ItAssetsSerializers(data = stu)
        if serializer.is_valid():
            serializer.save()
            return Response("data created")
        return Response("data not created")

    def update(self, request, pk):
        id = pk
        stu = ITAssetsModel.objects.get(id = id)
        serializer = ItAssetsSerializers(stu,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("data Updated")
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = ITAssetsModel.objects.get(id=id)
        serializer = ItAssetsSerializers(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("data Updated")
        return Response(serializer.errors)

    def destroy(self, request, pk):
        stu = ITAssetsModel.objects.get(id = pk)
        stu.delete()
        return Response("data deleted")
