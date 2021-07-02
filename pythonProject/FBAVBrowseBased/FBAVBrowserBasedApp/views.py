from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializers
from .models import Student
from rest_framework import status
# Create your views here.


@api_view(['POST','PUT','PATCH','GET','DELETE'])
def Student_Api(request, pk=None):
    if request.method == 'POST':
        data = request.data
        serilizer = StudentSerializers(data = data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data created'})
        return Response(serilizer.errors)
    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(id =id)
        serializer = StudentSerializers(stu, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated completly'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializers(stu, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated partialy'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer= StudentSerializers(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        if stu:
            serializer = StudentSerializers(stu, many= True )
            return Response(serializer.data)
        return Response({"msg":"No Data found"})

    if request.method == "DELETE":
        stu = Student.objects.get(id = pk)
        stu.delete()
        return Response({'msg':'data deleted'}, status=status.HTTP_200_OK)