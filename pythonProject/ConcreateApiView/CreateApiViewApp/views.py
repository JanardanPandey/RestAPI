from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudnetSerilizers

class LCConcreteAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudnetSerilizers

class RUDConcreteAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudnetSerilizers