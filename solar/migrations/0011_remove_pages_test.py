# Generated by Django 3.0.6 on 2020-09-02 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0010_auto_20200902_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pages',
            name='test',
        ),
    ]