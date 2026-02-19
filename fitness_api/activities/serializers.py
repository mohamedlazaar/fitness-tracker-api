from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def validate_duration_minutes(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be > 0 minutes")
        return value

    def validate_calories_burned(self, value):
        if value < 0:
            raise serializers.ValidationError("Calories cannot be negative")
        return value

    def validate(self, attrs):
        if not attrs.get('activity_type'):
            raise serializers.ValidationError("Activity type is required")
        if not attrs.get('date'):
            raise serializers.ValidationError("Date is required")
        return attrs
