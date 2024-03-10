from rest_framework import serializers
from merch.models import Merch
from content.serializers import ContentSerializer
from .models import (Ambassador,
                     Promocode,
                     WorkIt,
                     AmbassadorPromocode,
                     AmbassadorMerch)


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


class AddAmbassadorMerchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'merch')
        model = AmbassadorMerch

    def to_representation(self, instance):
        return GetAmbassadorMerchSerializer(
            instance,
            context={
                'request': self.context.get('request')
            }
        ).data


class GetAmbassadorSerializerLight(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'telegram')
        model = Ambassador


class GetAmbassadorMerchSerializer(serializers.ModelSerializer):
    ambassador = GetAmbassadorSerializerLight(read_only=True)
    merch = GetMerchSerializer(read_only=True)

    class Meta:
        fields = ('ambassador', 'merch')
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


class WorkItSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'is_blog', 'is_community', 'is_articles', 'is_video',
            'is_workshop', 'is_advice', 'is_events')
        model = WorkIt


class GetAmbassadorSerializer(serializers.ModelSerializer):
    promocodes = GetPromocodeSerializer(
        many=True, read_only=True, source='promocode'
    )
    merch = GetMerchSerializer(many=True, read_only=True)
    work_it = WorkItSerializer(read_only=True)
    content = ContentSerializer()

    class Meta:
        fields = (
            'id', 'telegram', 'first_name', 'last_name', 'second_name',
            'gender', 'course', 'country', 'city', 'address', 'postcode',
            'email', 'phone', 'education', 'status', 'work', 'purpose',
            'other', 'social', 'shirt_size', 'foot_size', 'work_it',
            'comments', 'promocodes', 'merch', 'guide', 'onboarding',
            'create_date', 'content'
        )
        # 'task'

        model = Ambassador


class AddAmbassadorSerializer(serializers.ModelSerializer):
    work_it = WorkItSerializer()

    class Meta:
        fields = (
            'telegram', 'first_name', 'last_name', 'second_name', 'gender',
            'course', 'country', 'city', 'address', 'postcode', 'email',
            'phone', 'education', 'work', 'purpose', 'other', 'social',
            'shirt_size', 'foot_size', 'work_it', 'comments', 'guide',
            'onboarding',
        )
        model = Ambassador

    def create(self, validated_data):
        work_it_data = validated_data.pop('work_it', None)
        purpose = validated_data.get('purpose', None)
        other = validated_data.get('other', None)

        if purpose != other:
            validated_data.pop('other', None)

        work_it = WorkIt.objects.create(**work_it_data)
        return Ambassador.objects.create(work_it=work_it, **validated_data)

    def update(self, instance, validated_data):
        work_it_data = validated_data.pop('work_it', None)
        purpose = validated_data.get('purpose', None)
        other = validated_data.get('other', None)

        if purpose != other:
            validated_data.pop('other', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            instance.save()

        if work_it_data:
            work_it_instance, created = WorkIt.objects.get_or_create(
                **work_it_data)
            instance.work_it = work_it_instance

        return instance

    def to_representation(self, instance):
        return GetAmbassadorSerializer(
            instance,
            context={
                'request': self.context.get('request')
            }
        ).data
