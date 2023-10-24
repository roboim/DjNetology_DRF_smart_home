# Generated by Django 4.2.6 on 2023-10-23 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='measurements',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
    ]