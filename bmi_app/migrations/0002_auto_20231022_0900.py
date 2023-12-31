# Generated by Django 3.2.22 on 2023-10-22 08:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bmi_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmirecord',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bmirecord',
            name='height',
            field=models.FloatField(default=True),
        ),
        migrations.AddField(
            model_name='bmirecord',
            name='weight',
            field=models.FloatField(default=True),
        ),
    ]
