from django.db import models

class Useful_Materials(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to="meterials_video", blank=True, null=True)
    image = models.FileField(upload_to="materials_photo", blank=True, null=True)
    app_link = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
