from rest_framework import viewsets

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing To-do items.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = []
