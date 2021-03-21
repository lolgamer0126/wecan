from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField(blank=True, null = True)
    preview = models.TextField(blank=True, null = True)
    def __str__(self):
        return self.title
    