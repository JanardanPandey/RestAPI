from django.shortcuts import render

# Create your views here.
from .models import StudentModels
from .serializers import StudentSerializers
from rest_framework import viewsets

class StudentViewSetReadonly(viewsets.ReadOnlyModelViewSet):
    queryset = StudentModels.objects.all()
    serializer_class = StudentSerializers