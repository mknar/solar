# Generated by Django 3.0.6 on 2020-09-02 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0011_remove_pages_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='test',
            field=models.CharField(blank=True, max_length=456),
        ),
    ]