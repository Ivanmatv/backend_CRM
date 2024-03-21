from rest_framework import viewsets, permissions

from .models import Tasks
from .serializers import TasksSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
