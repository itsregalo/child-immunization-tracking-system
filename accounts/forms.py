from django import forms
from .models import *


class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Doctor