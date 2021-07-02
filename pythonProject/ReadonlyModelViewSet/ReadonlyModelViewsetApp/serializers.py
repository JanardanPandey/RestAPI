from rest_framework import serializers
from .models import StudentModels

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentModels
        fields = '__all__'