from django.shortcuts import render

# Create your views here.
from .models import ItAssets
from .serializers import ItAssetsSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ItAssetAuthentication(viewsets.ModelViewSet):
    queryset = ItAssets.objects.all()
    serializer_class = ItAssetsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
