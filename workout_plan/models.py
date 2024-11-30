from django.db import models

class TrainingPlan(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.name


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
    exircices = models.TextField()

    def __str__(self):
        return f"{self.training_plan.name} - {self.day}"