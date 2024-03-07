# from rest_framework.generics import ListAPIView

# from tasks.serializers import TasksSerializer

# Задача связана с амбассадором Many-to-Many
# Нужно добавлять сериализатор для связанной модели в Ambassador


# class SubscriptionsView(ListAPIView):
#     serializer_class = TasksSerializer

#     def get_queryset(self):
#         return self.request.ambassador.tasks.all()
