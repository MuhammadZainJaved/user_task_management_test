from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from django.core.exceptions import PermissionDenied


class SuperuserOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        return request.user and request.user.is_superuser


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Task.objects.all()  # For superuser, show all tasks
        else:
            return Task.objects.filter(user=user)  # For normal user, show their tasks

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save(user=self.request.user)
        else:
            raise PermissionDenied("Only superusers can create tasks.")
