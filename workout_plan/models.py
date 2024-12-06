from django.db import models
from exercises.models import Exercise

class TrainingPlan(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    gender = models.CharField(max_length=30, choices= [('male', 'Male'), ('female', 'Female')])
    experience = models.CharField(max_length=30, choices= [('beginner', 'Beginner'),('fan', 'Fan'), ('pro', 'Pro')])
    intensity = models.CharField(max_length=30, choices = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])

    def __str__(self):
        return f"{self.name} - {self.gender} - {self.experience} - {self.intensity}"


class TrainingDay(models.Model):
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuestday', 'Tuestday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=40, choices=DAY_CHOICES)
    training_plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, related_name='days')
    description = models.TextField()
    exercises = models.ManyToManyField(Exercise, related_name="training_days")

    def __str__(self):
        return f"{self.training_plan.name} - {self.day}"