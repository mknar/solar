# Generated by Django 3.0.6 on 2020-09-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0009_auto_20200918_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='map',
            field=models.URLField(blank=True, null=True, verbose_name='Google map link'),
        ),
    ]
