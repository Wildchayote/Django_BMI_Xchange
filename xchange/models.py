from django.db import models

# Create your models here.
class Conversion(models.Model):

    POUND = 'GBP'
    NAIRA = 'NGN'
    UNITS = [
        (POUND, ('GBP')),
        (NAIRA, ('NGN')),
    ]
    currency = models.CharField( max_length=10, choices=UNITS, default=POUND)
    amount = models.FloatField(default=True, max_length=120)
    xchange = models.CharField( default=True, max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    