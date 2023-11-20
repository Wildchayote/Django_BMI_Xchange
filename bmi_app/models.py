from django.db import models

class BMIRecord(models.Model):
    name = models.CharField(default=False,max_length=120)
    height = models.FloatField(blank=False, null=True)
    weight = models.FloatField(blank=False, null=True)
    BMI = models.FloatField(blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True)

# class BMIRecord(models.Model):
#     height = models.FloatField(default=True)
#     weight = models.FloatField(default=True)
#     date = models.DateTimeField(auto_now_add=True)


# try:
#     # older Django
#     from django.utils.translation import ugettext_lazy as _, ugettext as gettext
# except ImportError:
#     # Django >= 3
#     from django.utils.translation import gettext_lazy as _, gettext

# class BMIRecord(models.Model):
#     USAGE_ONE_TIME = 'ONE_TIME'
#     USAGE_INFINITE = 'INFINITE'
#     USAGES = [
#         (USAGE_ONE_TIME, _('one-time only')),
#         (USAGE_INFINITE, _('infinite')),
#     ]
#     UNIT_PERCENTAGE = 'PERCENTAGE'
#     UNIT_CURRENCY = 'CURRENCY'
#     UNITS = [
#         (UNIT_PERCENTAGE, _('percentage')),
#         (UNIT_CURRENCY, _('currency')),
#     ]
#     height = models.FloatField(default=True)
#     weight = models.FloatField(default=True)
#     date = models.DateTimeField(auto_now_add=True)
#     code = models.CharField(_('code'), max_length=10, unique=True)
#     # amountt = models.PositiveSmallIntegerField(default=True,verbose_name=_('amount'))
#     unit = models.CharField(_('unit'), max_length=10, choices=UNITS, default=UNIT_PERCENTAGE)
#     usage = models.CharField(_('usage'), choices=USAGES, max_length=8)
#     description = models.CharField(_('description'), max_length=100)
#     valid_until = models.DateTimeField(_('valid until'), db_index=True, blank=True, null=True, default=None)
#     promoted = models.BooleanField(_('promoted'), default=False, help_text=_('show in topbar'))
#     add_to_cart = models.BooleanField(_('add to cart'), default=False, help_text=_('automatically'))
#     max_items = models.PositiveSmallIntegerField(_('max items in cart'), blank=True, null=True, default=None)

