from rest_framework import serializers
from .models import ITAssetsModel

class ItAssetsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ITAssetsModel
        fields = '__all__'