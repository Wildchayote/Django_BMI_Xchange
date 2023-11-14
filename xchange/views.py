from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConversionForm
from .models import Conversion
from django.http import Http404
import math
one_Npound = 1299.99
one_Pnaira = 1241.00

def mainform(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            conversion_record = form.save()
            return redirect('conversion_result', pk = conversion_record.pk)
    else:
        form = ConversionForm()
    return render(request, 'calculate.html', {'form': form})


def conversion_result(request, pk):
    conversion_record = get_object_or_404(Conversion,pk=pk)
    currency = conversion_record.currency
    amount = conversion_record.amount
    if currency == 'GBP':
        xchange = round((amount*one_Pnaira),2)
    else:
        xchange = round((amount/one_Npound),2)
        
    context= {'conversion_record': conversion_record,'convert' : xchange}
    
    conversion_res = Conversion(xchange = xchange, currency = currency, amount = amount)
    conversion_res.save()
    conversion_record.delete()
    pk-=1
    # if pk%2 !=0:
    #     conversion_res.delete()
    return render(request, 'conversion_res.html', context)
    

