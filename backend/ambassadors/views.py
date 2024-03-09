from rest_framework import mixins, viewsets, permissions
from django.shortcuts import get_object_or_404
from .models import Ambassador, Promocode, AmbassadorMerch, AmbassadorPromocode
from .serializers import (GetAmbassadorSerializer,
                          AddAmbassadorSerializer,
                          GetAmbassadorPromocodeSerializer,
                          AddAmbassadorPromocodeSerializer,
                          GetAmbassadorMerchSerializer,
                          AddAmbassadorMerchSerializer)


class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()
    filterset_fields = ('status', 'first_name', 'last_name', 'second_name',
                        'telegram', 'gender', 'course', 'promocode',
                        'onboarding', 'guide')
    search_fields = ('first_name', 'last_name', 'second_name', 'telegram',
                     'email', 'promocode__name')

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return GetAmbassadorSerializer
        return AddAmbassadorSerializer


class AmbassadorMerchViewSet(mixins.CreateModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return GetAmbassadorMerchSerializer
        return AddAmbassadorMerchSerializer

    def get_queryset(self):
        ambassador = get_object_or_404(Ambassador, pk=self.kwargs.get('id'))
        return AmbassadorMerch.objects.filter(
            ambassador=ambassador)

    def perform_create(self, serializer):
        ambassador = get_object_or_404(Ambassador, pk=self.kwargs.get('id'))
        return serializer.save(ambassador=ambassador)


class AmbassadorPromocodeViewSet(mixins.CreateModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return GetAmbassadorPromocodeSerializer
        return AddAmbassadorPromocodeSerializer

    def get_queryset(self):
        ambassador = get_object_or_404(Ambassador, pk=self.kwargs.get('id'))
        return AmbassadorPromocode.objects.filter(
            ambassador=ambassador)

    def perform_create(self, serializer):
        ambassador = get_object_or_404(Ambassador, pk=self.kwargs.get('id'))
        Promocode.objects.filter(
            promo_ambassador__ambassador=ambassador).update(status=False)
        return serializer.save(ambassador=ambassador)
