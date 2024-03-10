from rest_framework import viewsets

from content.serializers import ContentSerializer
from content.models import Contents


class ContentAmbassadorViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer

    def get_queryset(self):
        ambassador = self.kwargs.get("id")
        return Contents.objects.filter(ambassador=ambassador)
