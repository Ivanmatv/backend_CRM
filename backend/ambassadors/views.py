from rest_framework import mixins, viewsets
from .models import Ambassador, Promocode
from .serializers import AmbassadorSerializer, PromocodeSerializer


class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer


class PromocodeViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer
