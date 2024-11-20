from django.db import models
from authentication.models import CustomUser

class MealCalculation(models.Model):\

    GENDER_CHOICES = [
        ('male', 'Man'),
        ('female', 'Woman')           
    ]

    GOAL_CHOICES = [
        ('gain weight', 'Gain weight'),
        ('lose weight', 'Lose weight'),
        ('recomposition', 'Recomposition')

    ]

    ACTIVITY_CHOICES = [
        ('sedentary', 'Sedentary (little or no exercise)'),
        ('light', 'Lightly active (light exercise/sports 1-3 days/week)'),
        ('moderate', 'Moderately active (moderate exercise/sports 3-5 days/week)'),
        ('active', 'Very active (hard exercise/sports 6-7 days/week)'),
        ('very_active', 'Super active (very hard exercise/sports & physical job)')
    ]

    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE, null=True, blank=True)
    weight = models.FloatField()
    gender = models.CharField(max_length=14, choices = GENDER_CHOICES)
    goal = models.CharField(max_length=14, choices=GOAL_CHOICES)
    activity_level = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)

    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()

    calculated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} (Nutrition: {self.protein} g, {self.fat} g, {self.carbs} g)"