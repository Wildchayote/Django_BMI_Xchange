# Generated by Django 3.2.22 on 2023-11-04 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(default=True, max_length=120)),
                ('amount', models.FloatField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
