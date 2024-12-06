from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="training_days", blank=True, null=True)

    def __str__(self):
        return self.name
