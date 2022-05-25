from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def IndexView(request, *args, **kwargs):
    context = {

    }
    return render(request, 'index.html', context)

@login_required
def ParentDashboard(request, *args, **kwargs):
    context = {

    }
    return render(request, 'parent_dashboard.html', context)