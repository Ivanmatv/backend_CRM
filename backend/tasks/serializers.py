from django.contrib.auth import get_user_model
from rest_framework import serializers

from tasks.models import Tasks

User = get_user_model()


class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = (
            'title',
            'date_start',
            'date_end',
            'description',
            'status',
            'id',
            'user_id')
        read_only_fields = ('id',)
