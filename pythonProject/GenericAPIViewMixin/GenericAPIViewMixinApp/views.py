from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student
from .serializers import StudentSerializers
# Create your views here.

class StudentList(ListModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self,request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)


class StudentRetrive(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)


class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class StudentDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def delete(self, request, *args,**kwargs):
        return self.destroy(request, *args,**kwargs)