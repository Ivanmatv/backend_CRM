from rest_framework import mixins, viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Ambassador, Promocode, AmbassadorPromocode
from .serializers import (GetAmbassadorSerializer, AddAmbassadorSerializer,
                          GetPromocodeSerializer, AddPromocodeSerializer)


class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return GetAmbassadorSerializer
        return AddAmbassadorSerializer


class PromocodeViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):

    def get_queryset(self):
        ambassador = get_object_or_404(Ambassador, pk=self.kwargs.get('id'))
        return Promocode.objects.filter(
            promo_ambassador__ambassador=ambassador)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return GetPromocodeSerializer
        return AddPromocodeSerializer

    def perform_create(self, serializer):
        ambassador = get_object_or_404(Ambassador, pk=self.kwargs.get('id'))
        return serializer.save(ambassador=ambassador)
