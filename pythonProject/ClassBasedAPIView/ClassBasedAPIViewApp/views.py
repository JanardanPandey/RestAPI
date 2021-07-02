from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import decorators
from .serializers import StudentSerializers
from .models import Student
class StudentAPI(APIView):
    def post(self, request, format = None):
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data created', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,id=None, format = None):
        if id is not None:
            stu = Student.objects.get(id = id)
            serilizer = StudentSerializers(stu)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serilizer = StudentSerializers(stu, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)
    def put(self,request,id,format=None):
        stu = Student.objects.get(id=id)
        serializer = StudentSerializers(stu, request.body)
        if serializer.is_valid():
            serializer.save()
            return Response({"data updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)

    def patch(self,request, id, format = None):
        stu = Student.objects.get(id = id)
        serializer = StudentSerializers(stu, request.body, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)

    def delete(self,requeset, id, format = None):
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({'msg':'data deleted'},status=status.HTTP_202_ACCEPTED)