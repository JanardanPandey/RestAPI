
from rest_framework import serializers
from .models import Student

def start_with_r(value):
    if value[0].lower() != "r":
        raise serializers.ValidationError('Name must be start with R')

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators = [ start_with_r ])
    city = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.save()
        return instance
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Sheet Full')
        return value

    def validate(self, data):
        nm = data.get("name")
        ct = data.get("city")
        if nm.lower() == "krishna" and ct.lower() !="GKP":
            raise serializers.ValidationError("City must be belaura")
        return data

