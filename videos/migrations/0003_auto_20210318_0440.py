# Generated by Django 3.1.7 on 2021-03-18 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20210318_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
