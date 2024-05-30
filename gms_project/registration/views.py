from django.shortcuts import  redirect, render
from .forms import RegisterForm
from .models import Registers
def home(request):
    return render(request,'home.html')

def register(request):
     if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members_list')
     else:
        form = RegisterForm()
        return render(request, 'registration.html', {'form': form})
     
def members_list(request):
    members=Registers.objects.all()
    return render(request,'member_list.html',{'members':members})

def edit_member(request, member_id):
    member = Registers.objects.get(id=member_id) 
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members_list')
    else:
        form = RegisterForm(instance=member)
    return render(request, 'edit_registration.html', {'form': form})

def delete_member(request, member_id):
    member=Registers.objects.get(id=member_id)
    member.delete()
    return redirect('members_list')