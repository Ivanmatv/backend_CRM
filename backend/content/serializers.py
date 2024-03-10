from rest_framework import serializers

from content.models import Contents


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
