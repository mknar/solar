# Generated by Django 3.0.6 on 2020-09-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0008_auto_20200901_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pages',
            name='page_gallery',
        ),
        migrations.AddField(
            model_name='pages',
            name='page_gallery',
            field=models.ManyToManyField(blank=True, null=True, to='solar.gallery'),
        ),
    ]