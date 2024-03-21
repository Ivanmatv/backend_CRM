from rest_framework import viewsets

from .serializers import ContentSerializer
from .models import Content


class ContentAmbassadorViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

    def get_queryset(self):
        ambassador = self.kwargs.get("ambassador_id")
        return Content.objects.filter(ambassador=ambassador)
