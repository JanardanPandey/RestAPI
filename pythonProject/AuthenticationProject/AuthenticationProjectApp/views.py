from django.shortcuts import render
from rest_framework import viewsets
from .models import StudentAuthModel
from .seializers import StudentAuthSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
# Create your views here.
class StudentAuthView(viewsets.ModelViewSet):
    queryset = StudentAuthModel.objects.all()
    serializer_class = StudentAuthSerializer
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    #permission_classes = [IsAdminUser]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [DjangoModelPermissions]
