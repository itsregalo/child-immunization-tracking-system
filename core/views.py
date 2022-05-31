from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from accounts.models import *
from .forms import ChildCreateForm
from accounts.forms import DoctorRegistrationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def IndexView(request, *args, **kwargs):
    context = {

    }
    return render(request, 'index.html', context)

@login_required
def ParentDashboard(request, *args, **kwargs):
    parent = Parent.objects.get(user=request.user)
    parent_children = Child.objects.filter(parent=parent)

    context = {
        'parent': parent,
        'parent_children': parent_children,
    }
    return render(request, 'parent_dashboard.html', context)

@login_required
def parent_profile_settings(request, *args, **kwargs):
    parent = Parent.objects.get(user=request.user)
    context = {

    }
    return render(request, 'profile-settings.html', context)

@login_required
def dashboard_change_password(request, *args, **kwargs):
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if user.check_password(old_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password changed successfully')
                return HttpResponseRedirect(reverse('core:parent-dashboard'))
            messages.error(request, 'New password and confirm password does not match')     
    context = {

    }
    return render(request, 'dashboard_change_password.html', context)

@login_required
def doctor_dashboard(request, *args, **kwargs):
    doctor = Doctor.objects.get(user=request.user)
    doctor_children = Child.objects.filter(doctor=doctor)

    context = {
        'doctor': doctor,
        'doctor_children': doctor_children,
    }
    return render(request, 'doctor_dashboard.html', context)

@login_required
def doctor_children_assigned(request, *args, **kwargs):
    doctor = Doctor.objects.get(user=request.user)
    doctor_children = Child.objects.filter(doctor=doctor)

    context = {
        'doctor': doctor,
        'doctor_children': doctor_children,
    }
    return render(request, 'doctor_children_assigned.html', context)

@login_required
def doctor_appintments(request, *args, **kwargs):
    doctor = Doctor.objects.get(user=request.user)
    doctor_children = Child.objects.filter(doctor=doctor)

    context = {
        'doctor': doctor,
        'doctor_children': doctor_children,
    }
    return render(request, 'doctor_appointments.html', context)

@login_required
def doctor_profile_update(request, *args, **kwargs):
    doctor = Doctor.objects.get(user=request.user)
    form = DoctorRegistrationForm(request.POST or None, request.FILES or None, instance=doctor)
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return HttpResponseRedirect(reverse('core:doctor-dashboard'))
        messages.error(request, 'Profile update failed')

    context = {
        'doctor': doctor,
        'form':form
    }
    return render(request, 'doctor_profile_update.html', context)
    return render('doctor_profile_settings.html')

@login_required
def create_child(request, *args, **kwargs):
    parent = Parent.objects.get(user=request.user)
    if request.method == 'POST':
        form = ChildCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Child created successfully')
            return HttpResponseRedirect(reverse('core:parent-dashboard'))
    else:
        form = ChildCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'create_child.html', context)

@login_required
def child_profile(request, uuid, *args, **kwargs):
    child = Child.objects.get(uuid=uuid)
    immunizations = ChildImmunization.objects.all()
    context = {
        'child': child,
        'immunizations':immunizations
    }
    return render(request, 'child_profile.html', context)

@login_required
def child_profile_update(request, uuid, *args, **kwargs):
    child = Child.objects.get(uuid=uuid)
    if request.method == 'POST':
        form = ChildCreateForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            messages.success(request, 'Child profile updated successfully')
            return HttpResponseRedirect(reverse('core:parent-dashboard'))
    else:
        form = ChildCreateForm(instance=child)
    context = {
        'form': form,
    }
    return render(request, 'child_profile_update.html', context)