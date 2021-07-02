from rest_framework import serializers
from .models import StudentAuthModel

class StudentAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAuthModel
        fields = '__all__'