from rest_framework import serializers
from .models import Student

class StudnetSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','city','roll']