from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/')
    picture = models.ImageField(upload_to='photos/')
    def __str__(self):
        return self.title
    