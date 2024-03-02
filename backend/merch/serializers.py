from rest_framework import serializers

from drf_extra_fields.fields import Base64ImageField

from .models import Merch, Order


class MerchSerializer(serializers.ModelSerializer):
    """Serializer to read/update merchandises"""
    image = Base64ImageField(max_length=None)

    class Meta:
        model = Merch
        fields = (
            'size',
            'price',
            'name',
            'desc',
            'status',
            'category',
            'data_creation',
            'data_update',
            'image'
        )


class OrderSerializer(serializers.ModelField):
    """Serializer to read/update order"""

    class Meta:
        model = Order
        fields = (
            'name',
            'cost',
            'count',
            'date_creation'
        )
