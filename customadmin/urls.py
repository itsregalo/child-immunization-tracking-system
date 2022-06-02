from django.urls import path

from customadmin.views import *

app_name = 'custom-admin'

urlpatterns = [
    path('', IndexView, name='index'),
    path('doctors/', DoctorList, name='doctors')
]
