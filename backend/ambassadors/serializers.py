from rest_framework import serializers
from merch.models import Merch
from .models import Ambassador, Promocode, AmbassadorPromocode, AmbassadorMerch


class PromocodeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'date_start', 'date_end', 'name', 'status')
        model = Promocode


class AmbassadorSerializer(serializers.ModelSerializer):
    promocode_id = serializers.PrimaryKeyRelatedField(
        allow_null=True, queryset=Promocode.objects.all(), many=True
    )
    merch_id = serializers.PrimaryKeyRelatedField(
        allow_null=True, queryset=Merch.objects.all(), many=True
    )

    class Meta:
        fields = ('id', 'telegram', 'first_name', 'last_name',
                  'second_name', 'gender', 'course', 'country', 'city',
                  'address', 'email', 'phone', 'education', 'status', 'work',
                  'promocode_id', 'merch_id'
                  # 'content_id',
                  )
        model = Ambassador


class AmbassadorPromocodeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('pk', 'ambassador_id', 'promocode_id')
        model = AmbassadorPromocode


class AmbassadorMerchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('ambassador_id', 'merch_id')
        model = AmbassadorMerch
