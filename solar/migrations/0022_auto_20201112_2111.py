# Generated by Django 3.0.6 on 2020-11-12 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0021_auto_20201112_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subpage',
            old_name='slug',
            new_name='sub_slug',
        ),
    ]
