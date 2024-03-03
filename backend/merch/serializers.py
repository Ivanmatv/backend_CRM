from rest_framework import serializers

from drf_extra_fields.fields import Base64ImageField

from .models import Merch, Order, MerchOrder


class MerchSerializer(serializers.ModelSerializer):
    """Serializer to read/update merchandises"""
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Merch
        fields = (
            'id',
            'size_foot',
            'size_shirt',
            'price',
            'name',
            'desc',
            'quantity',
            'status',
            'category',
            'data_creation',
            'data_update',
            'image'
        )


class OrderSerializer(serializers.ModelSerializer):
    """Serializer to read/update order"""

    class Meta:
        model = Order
        fields = (
            'id',
            'name',
            'cost',
            'count',
            'date_creation'
        )


class MerchOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = MerchOrder
        fields = (
            'id',
            'merch',
            'order'
        )
