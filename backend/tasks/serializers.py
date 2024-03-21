from rest_framework import serializers

from tasks.models import Tasks


class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ('__all__')
        read_only_fields = ('id',)
