# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import BMIForm
# from .models import BMIRecord
# from django.http import Http404

# def calculate_bmi(request):
#     if request.method == 'POST':
#         form = BMIForm(request.POST)
#         if form.is_valid():
#             bmi_record = form.save()
#             return redirect('bmi_result', pk=bmi_record.pk)
#     else:
#         form = BMIForm()
#     return render(request, 'calculate_bmi.html', {'form': form})

# def bmi_result(request, pk):
#     bmi_record = get_object_or_404(BMIRecord,pk=pk)
#     height = bmi_record.height
#     weight = bmi_record.weight
#     bmi = weight / (height ** 2)
#     bmi_record.delete()
#     context = {'bmi_record': bmi_record, 'bmi': bmi}
#     return render(request, 'bmi_result.html', context)

#     # try:
#     #     bmi_record = BMIRecord.objects.get(pk=pk)
#     #     height = bmi_record.height
#     #     weight = bmi_record.weight
#     #     bmi = weight / (height ** 2)
#     #     return render(request, 'bmi_result.html', {'bmi_record': bmi_record, 'bmi': bmi})
#     # except BMIRecord.DoesNotExist:
#     #     raise Http404

# def home_view(request):
#     context =  {'BMI': 'BMI Page', 'xchange': 'Xchange Page'}
#     return render (request, 'home_page.html',context)



from django.shortcuts import render, redirect, get_object_or_404
from .forms import BMIForm
from .models import BMIRecord
import math



def calculate_bmi(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            bmi_record = form.save()
            return redirect('bmi_result', pk=bmi_record.pk)
    else:
        form = BMIForm()
    return render(request, 'calculate_bmi.html', {'form': form})

def bmi_result(request, pk):
    bmi_record = get_object_or_404(BMIRecord,pk=pk)
    name = bmi_record.name
    height = bmi_record.height
    weight = bmi_record.weight
    bmi = round((weight / (height ** 2)),2)
    
    bmi_result = BMIRecord(name=name, weight=weight, height=height, BMI=bmi)
    bmi_result.save()
    
    if pk%2 !=0:
        BMIRecord.objects.get(pk=pk).delete()
    return render(request, 'bmi_result.html', {'bmi_record': bmi_record, 'bmi': bmi, 'bmi_result': bmi_result})
