from rest_framework import serializers

from drf_extra_fields.fields import Base64ImageField

from .models import Merch, Order, MerchOrder


class MerchSerializer(serializers.ModelSerializer):
    """Serializer for the merchandise"""
    image = Base64ImageField(required=False, allow_null=True)
    size_foot = serializers.IntegerField(required=False)
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()

    class Meta:
        model = Merch
        fields = '__all__'

    def validate_size_foot(self, size_foot):
        if size_foot < 22 or size_foot > 33:
            raise serializers.ValidationError(
                "Размер обуви должен быть в промежутке от 22 до 33 см"
            )
        return size_foot

    def validate_quantity(self, quantity):
        if quantity < 1:
            raise serializers.ValidationError(
                "Количество должно быть больше 0"
            )
        return quantity

    def validate_price(self, price):
        if price < 1:
            raise serializers.ValidationError(
                "Цена должна быть больше 0"
            )
        return price


class GetOrderSerializer(serializers.ModelSerializer):
    """Read serializer order"""
    merchs = MerchSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_merchs(self, obj):
        return MerchSerializer(
            Merch.objects.filter(merch=obj),
            many=True,
        ).data


class AddOrderSerializer(serializers.ModelSerializer):
    """Serializer for the order"""
    cost = serializers.IntegerField()
    count = serializers.IntegerField()
    # merchs = MerchSerializer(many=True)
    merchs = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Merch.objects.all(),
        write_only=True)

    class Meta:
        model = Order
        fields = ('cost', 'count', 'name', 'merchs')
        read_only_fields = ('date_creation',)

    def validate_count(self, quantity):
        if quantity < 1:
            raise serializers.ValidationError(
                "Количество должно быть больше 0"
            )
        return quantity

    def validate_cost(self, price):
        if price < 1:
            raise serializers.ValidationError(
                "Стоймость должна быть больше 0"
            )
        return price

    # def create(self, validated_data):
    #     merchs_data = validated_data.pop('merchs')
    #     order = Order.objects.create(**validated_data)
    #     for merch_data in merchs_data:
    #         MerchOrder.objects.create(order=order, **merch_data)
    #     return order


class MerchOrderSerializer(serializers.ModelSerializer):
    """Serializer for the order of ambassador"""

    class Meta:
        model = MerchOrder
        fields = ('__all__')
