from django.shortcuts import render
from accounts.models import Doctor, Parent
from core.models import *
# Create your views here.

def IndexView(request):
    return render(request, 'admin-dash/index.html')

def DoctorList(request, *args, **kwargs):
    doctors = Doctor.objects.all()

    context = {
        'doctors':doctors
    }
    return render(request, 'admin-dash/doctors.html', context)

def DoctorDetail(request, pk):
    doctor = Doctor.objects.get(pk=pk)

    context = {
        'doctor':doctor
    }
    return render(request, 'admin-dash/doctor-detail.html', context)

def DoctorDelete(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    doctor.delete()

    return render(request, 'admin-dash/index.html')

def DoctorCreate(request, *args, **kwargs):
    return render(request, 'admin-dash/doctor-create.html')


def ParentList(request, *args, **kwargs):
    parents = Parent.objects.all()

    context = {
        'parents':parents
    }
    return render(request, 'admin-dash/parents.html', context)

def ParentDetail(request, pk):
    parent = Parent.objects.get(pk=pk)

    context = {
        'parent':parent
    }
    return render(request, 'admin-dash/parent-detail.html', context)

def ParentDelete(request, pk):
    parent = Parent.objects.get(pk=pk)
    parent.delete()

    return render(request, 'admin-dash/index.html')

def ParentCreate(request, *args, **kwargs):
    return render(request, 'admin-dash/parent-create.html')

def ChildList(request, *args, **kwargs):
    children = Child.objects.all()

    context = {
        'children':children
    }
    return render(request, 'admin-dash/children.html', context)

def ChildDetail(request, pk):
    child = Child.objects.get(pk=pk)

    context = {
        'child':child
    }
    return render(request, 'admin-dash/child-detail.html', context)

def ChildDelete(request, pk):
    child = Child.objects.get(pk=pk)
    child.delete()

    return render(request, 'admin-dash/index.html')

def ChildCreate(request, *args, **kwargs):
    return render(request, 'admin-dash/child-create.html')

def VaccinesList(request, *args, **kwargs):
    vaccines = Vaccines.objects.all()

    context = {
        'vaccines':vaccines
    }
    return render(request, 'admin-dash/vaccines.html', context)

def VaccinesDetail(request, pk):
    vaccine = Vaccines.objects.get(pk=pk)

    context = {
        'vaccine':vaccine
    }
    return render(request, 'admin-dash/vaccines-detail.html', context)

def VaccinesDelete(request, pk):
    vaccine = Vaccines.objects.get(pk=pk)
    vaccine.delete()

    return render(request, 'admin-dash/index.html')

def VaccinesCreate(request, *args, **kwargs):
    return render(request, 'admin-dash/vaccines-create.html')