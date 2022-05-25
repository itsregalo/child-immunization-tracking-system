from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from accounts.models import *

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