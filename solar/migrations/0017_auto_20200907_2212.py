# Generated by Django 3.0.6 on 2020-09-07 18:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0016_auto_20200907_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
