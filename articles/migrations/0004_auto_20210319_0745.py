# Generated by Django 3.1.7 on 2021-03-19 07:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]