from rest_framework import serializers

from drf_extra_fields.fields import Base64ImageField

from .models import Merch, Order, MerchOrder


class MerchSerializer(serializers.ModelSerializer):
    """Serializer to read/update merchandises"""
    image = Base64ImageField(required=False, allow_null=True)
    size_foot = serializers.IntegerField()

    class Meta:
        model = Merch
        fields = ('__all__')

    def validate_size_foot(self, size_foot):
        if size_foot < 22 or size_foot > 33:
            raise serializers.ValidationError(
                "Размер обуви должен быть в промежутке от 22 до 33 см"
            )
        return size_foot


class OrderSerializer(serializers.ModelSerializer):
    """Serializer to read/update order"""

    class Meta:
        model = Order
        fields = ('__all__')


class MerchOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = MerchOrder
        fields = ('__all__')
