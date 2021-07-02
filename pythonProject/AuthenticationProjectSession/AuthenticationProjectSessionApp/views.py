from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions,IsAdminUser
from .custompermission import CustomPermission

# Create your views here.
class StudentApi(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAuthenticated]
    permission_classes = [CustomPermission]
