# Generated by Django 3.1.7 on 2021-03-22 06:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20210318_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Video'),
        ),
    ]
