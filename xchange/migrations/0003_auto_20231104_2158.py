# Generated by Django 3.2.22 on 2023-11-04 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xchange', '0002_alter_conversion_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversion',
            name='amount',
            field=models.FloatField(default=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='conversion',
            name='currency',
            field=models.CharField(choices=[('Pound (£)', '£'), ('Naira (N)', 'N')], default='Pound (£)', max_length=10),
        ),
    ]
