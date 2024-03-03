from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from .models import Merch, Order, MerchOrder

from .serializers import MerchSerializer, OrderSerializer, MerchOrderSerializer


class MerchViewSet(viewsets.ModelViewSet):
    """Merchandise presentation"""
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('name', )


class OrderViewSet(viewsets.ModelViewSet):
    """Order presentation"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('name', )


class MerchOrderViewSet(viewsets.ModelViewSet):
    """Order presentation"""
    queryset = MerchOrder.objects.all()
    serializer_class = MerchOrderSerializer
