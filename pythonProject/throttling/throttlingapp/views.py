from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import PinkuRateThrottle
# Create your views here.


class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    #throttle_classes = [AnonRateThrottle,UserRateThrottle ]
    throttle_classes = [AnonRateThrottle,PinkuRateThrottle ]