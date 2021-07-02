from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers

@api_view(['GET','PUT','POST','DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        stu = request.data
        serializer = StudentSerializers(data = stu)
        if serializer.is_valid():
            serializer.save()
            return Response( {'msg':'data created'})
        return Response(serializer.errors)


    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializers(stu, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({'msg':'data deleted'})