from django.contrib import admin
from .models import Articles
# Register your models here.
admin.site.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['id','title']