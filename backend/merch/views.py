from rest_framework import viewsets, permissions

from .models import Merch, Order, MerchOrder

from .serializers import (MerchSerializer,
                          GetOrderSerializer,
                          AddOrderSerializer,
                          MerchOrderSerializer)


class MerchViewSet(viewsets.ModelViewSet):
    """Merchandise presentation"""
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """Order presentation"""
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return GetOrderSerializer
        return AddOrderSerializer


class MerchOrderViewSet(viewsets.ModelViewSet):
    """Representation of the order merchandise"""
    queryset = MerchOrder.objects.all()
    serializer_class = MerchOrderSerializer
