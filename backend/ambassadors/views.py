from rest_framework import mixins, viewsets, permissions
from django.shortcuts import get_object_or_404
from .models import Ambassador, AmbassadorMerch, AmbassadorPromocode
from .serializers import (GetAmbassadorSerializer,
                          AddAmbassadorSerializer,
                          GetAmbassadorPromocodeSerializer,
                          AddAmbassadorPromocodeSerializer,
                          AddAmbassadorMerchSerializer,
                          GetAmbassadorMerchSerializer)


class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return GetAmbassadorSerializer
        return AddAmbassadorSerializer


class AmbassadorMerchViewSet(mixins.CreateModelMixin,
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
        return serializer.save(ambassador=ambassador)
