from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET','POST','PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def Student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Posted")
        return Response(serializer.errors)