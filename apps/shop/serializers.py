from rest_framework import serializers
from apps.shop.models import Product


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    age = serializers.IntegerField()
    country = serializers.CharField(max_length=50)
