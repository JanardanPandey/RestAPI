from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','city','roll']


#fields = '__all__'
#exclude = ['roll']