from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Package

from .forms import PackageForm

# Create your views here.
def create_package(request):
    if request.method=='POST':
        package_form=PackageForm(request.POST)
        if package_form.is_valid():
            package_form.save()
            return HttpResponse("package added")
        else:
            return render(request, 'membership/create_package.html', {'package_form': package_form})
    else:
        package_form=PackageForm()
    return render(request,'membership/create_package.html',{'package_form':package_form})

def view_packages(request):
    packages=Package.objects.all()
    return render(request,'membership/view_packages.html',{'packages':packages})

def edit_packages(request,package_id):
    package=Package.objects.get(id=package_id)
    if request.method == 'POST':
        package_form=PackageForm(request.POST,instance=package)
        if package_form.is_valid():
            package_form.save()
            return redirect('view_packages')
        else:
            return render(request,'membership/edit_packages.html',{'package_form':package_form})    

        
    else:
        package_form = PackageForm(instance=package)
        return render(request,'membership/edit_packages.html',{'package_form':package_form})    





    