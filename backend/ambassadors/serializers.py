from rest_framework import serializers
from merch.models import Merch
from .models import Ambassador, Promocode, AmbassadorPromocode, AmbassadorMerch


class GetPromocodeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'date_start', 'name', 'status')
        model = Promocode


class AddPromocodeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('date_end', 'name', 'status')
        model = Promocode

    def create(self, validated_data):
        ambassador = validated_data.pop('ambassador')

        promocode = Promocode.objects.create(**validated_data)

        AmbassadorPromocode.objects.create(
            ambassador=ambassador, promocode=promocode)

        return promocode


class GetMerchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'desc', 'size_foot', 'size_shirt', 'price',
                  'quantity', 'data_creation', 'data_update')
        model = Merch


class AmbassadorMerchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('pk', 'merch')
        model = AmbassadorMerch


class GetAmbassadorPromocodeSerializer(serializers.ModelSerializer):
    promocodes = GetPromocodeSerializer(read_only=True, source='promocode')

    class Meta:
        fields = ('ambassador', 'promocodes')
        model = AmbassadorPromocode


class AddAmbassadorPromocodeSerializer(serializers.ModelSerializer):
    promocode = AddPromocodeSerializer()

    class Meta:
        fields = ('promocode',)
        model = AmbassadorPromocode

    def create(self, validated_data):
        ambassador = validated_data.pop('ambassador')
        promocode = validated_data.pop('promocode')
        print(promocode)

        promocode = Promocode.objects.create(**promocode)

        AmbassadorPromocode.objects.create(
            ambassador=ambassador, promocode=promocode)

        return promocode

    def to_representation(self, instance):
        return GetPromocodeSerializer(
            instance,
            context={
                'request': self.context.get('request')
            }
        ).data


class GetAmbassadorSerializer(serializers.ModelSerializer):
    promocodes = GetPromocodeSerializer(
        many=True, read_only=True, source='promocode'
    )
    merch = GetMerchSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            'id', 'telegram', 'first_name', 'last_name', 'second_name',
            'gender', 'course', 'country', 'postcode', 'city', 'address',
            'email', 'phone', 'education', 'status', 'work', 'purpose',
            'social', 'shirt_size', 'foot_size', 'promocodes', 'merch',
            'comments', 'create_date', 'completed_guide'
        )
        # 'content',

        model = Ambassador


class AddAmbassadorSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id', 'telegram', 'first_name', 'last_name', 'second_name',
            'gender', 'course', 'country', 'postcode', 'city', 'address',
            'email', 'phone', 'education', 'work', 'purpose', 'social',
            'shirt_size', 'foot_size', 'comments',
        )
        model = Ambassador

    def to_representation(self, instance):
        return GetAmbassadorSerializer(
            instance,
            context={
                'request': self.context.get('request')
            }
        ).data
