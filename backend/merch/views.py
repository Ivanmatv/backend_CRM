from rest_framework import filters, status, viewsets

from django_filters.rest_framework import DjangoFilterBackend

from .models import Merch, Order

from .serializers import MerchSerializer, OrderSerializer


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
