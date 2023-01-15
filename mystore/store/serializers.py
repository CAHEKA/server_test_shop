from .models import Products
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.StringRelatedField(many=True)

    class Meta:
      model= Products
      fields = ['id', 'name', 'slug', 'image', 'price',
                'qty', 'inventory', 'description', 'rating']
