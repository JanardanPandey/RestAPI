from django.shortcuts import render
from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializers
# Create your views here.

class StudentApi(viewsets.ModelViewSet):
    querysets = Student.objects.all()
    serializer_class = StudentSerializers