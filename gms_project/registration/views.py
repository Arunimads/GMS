from django.http import HttpResponse
from django.shortcuts import  redirect, render
from .forms import RegisterForm, TrainerRegisterForm, UserForm
from .models import MemberRegisters, TrainerRegisters
from django.contrib.auth.decorators import login_required


@login_required
def register(request):
     if request.method == 'POST':
        user_form=UserForm(request.POST)
        member_form = RegisterForm(request.POST)
        if member_form.is_valid() and user_form.is_valid():
            user=user_form.save(commit=False)
            user.is_active=False
            user.set_password(user_form.cleaned_data['password'])
            user.save()  
            member=member_form.save(commit=False)   
            member.user=user       
            member.save()
            return redirect('members_list')
        else:
            return HttpResponse("<script>window.alert('Not saved');window.location.href='/register/'</script>")
     else:
        user_form = UserForm()
        member_form = RegisterForm()
        return render(request, 'registration/registration.html', {'member_form': member_form,'user_form':user_form})
     
def members_list(request):
    members=MemberRegisters.objects.all()
    return render(request,'registration/member_list.html',{'members':members})

def edit_member(request, member_id):
    member = MemberRegisters.objects.get(id=member_id) 
    if request.method == 'POST':
        member_form = RegisterForm(request.POST, instance=member)
        if member_form.is_valid():
            member_form.save()
            return redirect('members_list') 
    else:
        member_form = RegisterForm(instance=member)
    return render(request, 'registration/edit_registration.html', {'member_form': member_form})

def delete_member(request, member_id):
    member=MemberRegisters.objects.get(id=member_id)
    member.delete()
    return redirect('members_list')

def approve_member(request, member_id):
    member = MemberRegisters.objects.get(id=member_id)
    user = member.user
    user.is_active = True
    user.save()
    return redirect('members_list')

def disapprove_member(request, member_id):
    member = MemberRegisters.objects.get(id=member_id)
    user = member.user
    user.is_active = False
    user.save()
    return redirect('members_list')


def add_trainer(request):
     if request.method == 'POST':
        user_form=UserForm(request.POST)
        trainer_form =TrainerRegisterForm(request.POST)
        if trainer_form.is_valid() and user_form.is_valid():
            user=user_form.save(commit=False)
            user.is_active=False
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            trainer=trainer_form.save(commit=False)
            trainer.user=user
            trainer.save()
            return HttpResponse("<script>window.alert('trainer added');window.location.href='/trainer_list/'</script>")

     else:
        user_form = UserForm()
        trainer_form =TrainerRegisterForm()
        return render(request, 'registration/add_trainer.html', {'trainer_form': trainer_form,'user_form':user_form})
     
def trainer_list(request):
    trainers=TrainerRegisters.objects.all()
    return render(request,'registration/trainer_list.html',{'trainers':trainers})

def edit_trainer(request, trainer_id):
    trainer = TrainerRegisters.objects.get(id=trainer_id) 
    if request.method == 'POST':
        trainer_form = TrainerRegisterForm(request.POST, instance=trainer)
        if trainer_form.is_valid():
            trainer_form.save()
            return redirect('trainer_list')
    else:
        trainer_form = TrainerRegisterForm(instance=trainer)
    return render(request, 'registration/edit_trainer.html', {'trainer_form': trainer_form})

def delete_trainer(request, trainer_id):
    trainer=TrainerRegisters.objects.get(id=trainer_id)
    trainer.delete()
    return redirect('trainer_list')


