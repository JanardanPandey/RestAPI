from django.shortcuts import render
from  .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
# Create your views here.

class StudentMixin(GenericAPIView, ListModelMixin, CreateModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    def get(self, request, *args, **kwargs ):
        return self.list(request, *args, **kwargs)
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StudentMixinPK(GenericAPIView, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)