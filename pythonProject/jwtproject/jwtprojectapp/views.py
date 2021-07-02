from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
#from jwtprojectapp.CustomAuth import CustomAuth

from rest_framework import viewsets

class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    #authentication_classes = [CustomAuth]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]