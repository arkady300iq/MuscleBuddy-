from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from workout_plan.models import TrainingPlan

class Preferences(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner'),
        ('fan', 'Fan'),
        ('pro', 'Pro'),
    ]

    INTENSITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES)
    experience = models.CharField(max_length=10, choices = EXPERIENCE_CHOICES)
    intensity = models.CharField(max_length=10, choices = INTENSITY_CHOICES)
    plan = models.ForeignKey(TrainingPlan, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.gender} - {self.experience} - {self.intensity}"
    
