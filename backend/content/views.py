from rest_framework import viewsets

from content.serializers import ContentSerializer
from content.models import Contents


class ContentAmbassadorView(viewsets.ModelViewSet):
    serializer_class = ContentSerializer

    def get_queryset(self):
        ambassador_id = self.kwargs.get("ambassador_id")
        new_queryset = Contents.objects.filter(ambassador=ambassador_id)
        return new_queryset
