from rest_framework import serializers
from .models import SpuInfo


class SpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpuInfo
        fields = '__all__'
