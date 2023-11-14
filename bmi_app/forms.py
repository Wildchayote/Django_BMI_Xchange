from django import forms
from .models import BMIRecord

class BMIForm(forms.ModelForm):
    class Meta:
        model = BMIRecord
        fields = ['height', 'weight']
        # fields = ['height', 'weight','code','unit', 'usage','description',
        #           'valid_until','promoted','add_to_cart','max_items']
