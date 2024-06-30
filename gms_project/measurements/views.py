from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Measurements

from .forms import MeasurementForm


# Create your views here.

def add_measurements(request):
    if request.method=='POST':
        measurement_form=MeasurementForm(request.POST)
        if measurement_form.is_valid():
            measurement = measurement_form.save(commit=False)
            measurement.user = request.user  
            measurement.save()
            # return redirect('measurement_list')
            return HttpResponse('added measurements')
    else:
       measurement_form=MeasurementForm()
       return render(request,'measurements/add_measurements.html',{'measurement_form':measurement_form})

def view_measurements(request):
    measurement=Measurements.objects.all()
    return render(request,"measurements/view_measurements.html",{'measurements':measurement})   

