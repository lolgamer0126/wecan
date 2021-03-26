from django.db import models
from cloudinary_storage.validators import validate_video
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.CharField(max_length=200)  
    picture = models.ImageField(upload_to='photos/')
    def __str__(self):
        return self.title
        