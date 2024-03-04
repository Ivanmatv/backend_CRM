from rest_framework import serializers
# from merch.models import Merch
from .models import Ambassador, Promocode, AmbassadorPromocode, AmbassadorMerch, Merch


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


class AmbassadorPromocodeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('ambassador', 'promocode')
        model = AmbassadorPromocode


class GetAmbassadorSerializer(serializers.ModelSerializer):
    promocodes = GetPromocodeSerializer(
        many=True, read_only=True, source='promocode'
    )
    merch = serializers.PrimaryKeyRelatedField(
        queryset=Merch.objects.all(), many=True, required=False
    )

    class Meta:
        fields = ('id', 'telegram', 'first_name', 'last_name',
                  'second_name', 'gender', 'course', 'country', 'city',
                  'address', 'email', 'phone', 'education', 'status', 'work',
                  'promocodes', 'merch'
                  # 'content',
                  )
        model = Ambassador


class AddAmbassadorSerializer(serializers.ModelSerializer):
    promocodes = AddPromocodeSerializer(
        many=False, required=False, source='promocode'
    )
    merch = serializers.PrimaryKeyRelatedField(
        queryset=Merch.objects.all(), many=True, required=False
    )

    class Meta:
        fields = ('id', 'telegram', 'first_name', 'last_name',
                  'second_name', 'gender', 'course', 'country', 'city',
                  'address', 'email', 'phone', 'education', 'status', 'work',
                  'promocodes', 'merch'
                  # 'content',
                  )
        model = Ambassador

    def create(self, validated_data):
        promocode_data = validated_data.pop('promocode', None)
        merch_data = validated_data.pop('merch', None)

        ambassador = Ambassador.objects.create(**validated_data)

        if promocode_data:
            promocode, status = Promocode.objects.get_or_create(
                **promocode_data)

            AmbassadorPromocode.objects.create(
                ambassador=ambassador, promocode=promocode)

        if merch_data:
            ambassador.merch.set(merch_data)

        return ambassador

    def to_representation(self, instance):
        return GetAmbassadorSerializer(
            instance,
            context={
                'request': self.context.get('request')
            }
        ).data


class AmbassadorMerchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('pk', 'ambassador', 'merch')
        model = AmbassadorMerch

