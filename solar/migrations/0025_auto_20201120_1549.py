# Generated by Django 3.0.6 on 2020-11-20 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0024_pages_main_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='main_page',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='solar.pages'),
        ),
    ]