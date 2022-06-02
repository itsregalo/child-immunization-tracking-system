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

def ParentList(request, *args, **kwargs):
    parents = Parent.objects.all()

    context = {
        'parents':parents
    }
    return render(request, 'admin-dash/parents.html', context)

def ChildList(request, *args, **kwargs):
    children = Child.objects.all()

    context = {
        'children':children
    }
    return render(request, 'admin-dash/children.html', context)

def VaccinesList(request, *args, **kwargs):
    vaccines = Vaccines.objects.all()

    context = {
        'vaccines':vaccines
    }
    return render(request, 'admin-dash/vaccines.html', context)