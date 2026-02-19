from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count
from .models import Activity
from .serializers import ActivitySerializer

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    # Built-in DRF ordering (from ALX concept)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'duration_minutes', 'calories_burned']
    ordering = ['-date']  # newest first

    def get_queryset(self):
        """
        1. Filter against current user (ALX example 1)
        2. Filter against query parameters (ALX example 3)
        """
        # Start with only current user's activities
        queryset = Activity.objects.filter(user=self.request.user)

        # Filter by activity_type (query param)
        activity_type = self.request.query_params.get('activity_type')
        if activity_type:
            queryset = queryset.filter(activity_type=activity_type)

        # Filter by date range (query param)
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        """
        Metrics endpoint (spec requirement)
        """
        qs = self.get_queryset()
        totals = qs.aggregate(
            total_activities=Count('id'),
            total_duration=Sum('duration_minutes'),
            total_distance=Sum('distance_km'),
            total_calories=Sum('calories_burned'),
        )
        return Response({
            'total_activities': totals['total_activities'] or 0,
            'total_duration_minutes': totals['total_duration'] or 0,
            'total_distance_km': float(totals['total_distance'] or 0),
            'total_calories_burned': totals['total_calories'] or 0,
        })
