from .models import Orders
from rest_framework import serializers


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = ['cart', 'state', 'subtotal', 'tax', 'total']
