from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255, choices=[('running', 'Running'), ('cycling', 'Cycling'), ('swimming', 'Swimming'), ('walking', 'Walking'), ('other', 'Other')])
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField()
    calories_burned = models.IntegerField()
    date = models.DateField()
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type} - {self.date}"