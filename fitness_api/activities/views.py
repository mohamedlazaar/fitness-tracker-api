from rest_framework import viewsets, permissions
from .models import Activity
from .serializers import ActivitySerializer

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Activity.objects.filter(user=self.request.user)
        return Activity.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
