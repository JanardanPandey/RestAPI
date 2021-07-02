from rest_framework import serializers
from .models import ItAssets
class ItAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItAssets
        fields = '__all__'