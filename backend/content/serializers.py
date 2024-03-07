from django.contrib.auth import get_user_model
from rest_framework import serializers

from content.models import Contents

User = get_user_model()


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contents
        fields = (
            'name',
            'platform',
            'link',
            'guide',
            'description',
            'status',
            'id',
            'ambassador')
        read_only_fields = ('id',)
