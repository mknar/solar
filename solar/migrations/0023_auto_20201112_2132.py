# Generated by Django 3.0.6 on 2020-11-12 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0022_auto_20201112_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subpage',
            name='main_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_pages', to='solar.pages'),
        ),
    ]
