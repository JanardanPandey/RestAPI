from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
# Create your views here.
class studentapi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers