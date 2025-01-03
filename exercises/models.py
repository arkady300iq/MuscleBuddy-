from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    description_set = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="training_days/", blank=True, null=True)
    video_file = models.FileField(upload_to="exercise_videos/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']  

    def __str__(self):
        return self.name