from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializers
# Create your views here.
from rest_framework import viewsets

class StudentViewsets(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers